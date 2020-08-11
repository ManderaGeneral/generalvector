
from generalvector import Vec2, Vec
from generalvector.general import GeneralVector


from generallibrary import getLocalFeaturesAsMD


# print(getLocalFeaturesAsMD(locals(), "generalvector"))


d = dict(Vec2.__dict__)
d.update(dict(Vec.__dict__))
d.update(dict(GeneralVector.__dict__))


print(getLocalFeaturesAsMD(d, "generalvector"))
