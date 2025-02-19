from dataclasses import dataclass, field, replace, Field, is_dataclass


def imns(cls):
    '''Immutible Namespace, one honking great idea'''
    # For members to be opperated apon, they must have type declerations

    # This finds the fileds that are in vanila class
    # so that this class decorater doesnt intafear with
    # normal python machenary.
    class Dummy:
        pass

    types = cls.__annotations__

    for name, val, type in [(name, val, types[name])
                            for name, val in cls.__dict__.items()
                            if name in types
                            and name not in set(Dummy.__dict__) | {'__annotations__'}]:

        if is_dataclass(type):
            if val is None:
                # if a dataclass is not given a value, then the dataclass its self becomes hte default factory
                val = field(default_factory=type)
            elif isinstance(val, dict):
                # if the value is a dictionary, but then the a dataclass is used as the default initialised with the arguments in the dictionary
                val = field(default=type(**val))
            elif isinstance(val, Field):
                val = val
            elif callable(val):
                val = field(default_factory=val)
            else:
                assert False, ("unsupported default type", cls, name, type, val)
        else:
            if val is None: continue
            if callable(val):
                val = field(default_factory=val)
            else:
                val = field(default=val)

        setattr(cls, name, val)

    cls.__call__ = replace
    return dataclass(cls, frozen=True)
