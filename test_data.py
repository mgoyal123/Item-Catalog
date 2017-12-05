from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Game, Base, GameItem, User

engine = create_engine('sqlite:///gamecatalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Mishu Goyal", email="mishugoyal11@gmail.com", picture='http'
             '://storagebythefox.com.au/wp-content/uploads/2016/11/placeholder'
             '.jpg')
session.add(User1)
session.commit()


# Items for Soccer
game1 = Game(user_id=1, name="Soccer")

session.add(game1)
session.commit()

gameItem1 = GameItem(user_id=1, name="Two shinguards", description="A shin "
                     "guard or shin pad is a piece of equipment worn on the "
                     "front of a player's shin to protect them from injury. "
                     "These are commonly used in sports including association "
                     "football (soccer), baseball, ice hockey, field hockey, "
                     "lacrosse, cricket, and other sports.", game=game1)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Soccer cleats", description="Cleats or "
                     "studs are protrusions on the sole of a shoe, or on an "
                     "external attachment to a shoe, that provide additional "
                     "traction on a soft or slippery surface. ", game=game1)

session.add(gameItem2)
session.commit()

User2 = User(name="Saurabh Goyal", email="saurabh@gmail.com", picture='https:'
             '//thumb1.shutterstock.com/display_pic_with_logo/2409857/40016692'
             '0/stock-vector--avatar-profile-icon-man-400166920.jpg')
session.add(User2)
session.commit()
# Items for Basketball
game2 = Game(user_id=2, name="Basketball")

session.add(game2)
session.commit()

gameItem1 = GameItem(user_id=2, name="Ball", description="A basketball is a "
                     "spherical ball used in basketball games.... The standard"
                     " for a basketball in the NBA is 29.5 inches (75 cm) in "
                     "circumference. Aside from the court and the baskets,the"
                     " basketball is the only piece of equipment necessary to"
                     " play the game of basketball.", game=game2)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=2, name="Backboard", description="A backboard is"
                     " a piece of basketball equipment. It is a raised vertic"
                     "al board with a basket attached. It is made of a flat, "
                     "rigid piece of, often Plexiglas or tempered glass which"
                     " also has the properties of safety glass when accidenta"
                     "lly shattered.", game=game2)

session.add(gameItem2)
session.commit()

User3 = User(name="Vishu Goyal", email="vishu.goyal.7@gmail.com", picture='ht'
             'tp://storagebythefox.com.au/wp-content/uploads/2016/11/placehol'
             'der.jpg')
session.add(User3)
session.commit()

# Items for Baseball
game3 = Game(user_id=3, name="Baseball")

session.add(game3)
session.commit()

gameItem1 = GameItem(user_id=3, name="Bat", description="A rounded, solid woo"
                     "den or hollow aluminum bat. Wooden bats are traditional"
                     "ly made from ash wood, though maple and bamboo is also "
                     "sometimes used. Aluminum bats are not permitted in prof"
                     "essional leagues, but are frequently used in amateur le"
                     "agues. Composite bats are also available, essentially w"
                     "ooden bats with a metal rod inside. Bamboo bats are als"
                     "o becoming popular.", game=game3)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=3, name="Batting Helmet", description="Helmet wo"
                     "rn by batter to protect the head and the ear facing the"
                     " pitcher from the ball. Professional models have only o"
                     "ne ear protector (left ear for right-handed batters, ri"
                     "ght ear for lefties), amateur and junior helmets usuall"
                     "y have ear protectors on both sides, for better protect"
                     "ion from loose balls, and to reduce costs to teams (all"
                     " players can use the same style of helmet)", game=game3)

session.add(gameItem2)
session.commit()

# Items for Frisbee
game4 = Game(user_id=1, name="Frisbee")

session.add(game4)
session.commit()

gameItem1 = GameItem(user_id=1, name="Flying Disc", description="A frisbee (a"
                     "lso called a flying disc or simply a disc) is a gliding"
                     " toy or sporting item that is generally plastic and rou"
                     "ghly 20 to 25 centimetres (8 to 10 in) in diameter with"
                     " a lip,[1] used recreationally and competitively for th"
                     "rowing and catching, for example, in flying disc games."
                     " The shape of the disc, an airfoil in cross-section, al"
                     "lows it to fly by generating lift as it moves through t"
                     "he air while spinning.", game=game4)

session.add(gameItem1)
session.commit()

# Items for Snowboarding
game5 = Game(user_id=2, name="Snowboarding")

session.add(game5)
session.commit()

gameItem1 = GameItem(user_id=2, name="Snowboard", description="Snowboards are"
                     " typically flat pieces of plywood painted a light color"
                     " (most commonly white), around 16 to 24 in (41 to 61 cm"
                     ") in length and width and around 0.5 to 0.75 in (1.3 to"
                     " 1.9 cm) thick.[2][3][4][5] In addition the Weaverboard"
                     " used in Canada has a white stick with a black tip plac"
                     "ed in the centre. This allows for the board to be found"
                     " if the newly fallen snow was to completely cover the b"
                     "oard.", game=game5)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=2, name="Goggles", description="Snow goggles are"
                     " a type of eyewear traditionally used by the Inuit and "
                     "the Yupik, formerly known as Eskimo, peoples of the Arc"
                     "tic to prevent snow blindness.The goggles are tradition"
                     "ally made of driftwood (especially spruce), bone, walru"
                     "s ivory, caribou antler or in some cases seashore grass",
                     game=game5)

session.add(gameItem2)
session.commit()

# Items for Rock climbing
game6 = Game(user_id=1, name="Rock Climbing")

session.add(game6)
session.commit()


gameItem1 = GameItem(user_id=1, name="Rope", description="Climbing ropes are "
                     "typically of kernmantle construction, consisting of a c"
                     "ore (kern) of long twisted fibres and an outer sheath ("
                     "mantle) of woven coloured fibres. The core provides abo"
                     "ut 80% of the tensile strength, while the sheath is a d"
                     "urable layer that protects the core and gives the rope "
                     "desirable handling characteristics.", game=game6)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Carbiners", description="Carabiners are"
                     " metal loops with spring-loaded gates (openings), used "
                     "as connectors. Once made primarily from steel, almost a"
                     "ll carabiners for recreational climbing are now made fr"
                     "om a light weight aluminum alloy. Steel carabiners are "
                     "much heavier, but harder wearing, and therefore are oft"
                     "en used by instructors when working with groups.",
                     game=game6)

session.add(gameItem2)
session.commit()

gameItem3 = GameItem(user_id=1, name="QuickDraws", description="Quickdraws (o"
                     "ften referred to as \"draws\") are used by climbers to "
                     "connect ropes to bolt anchors, or to other traditional "
                     "protection, allowing the rope to move through the ancho"
                     "ring system with minimal friction. A quickdraw consists"
                     " of two non-locking carabiners connected together by a "
                     "short, pre-sewn loop of webbing.", game=game6)

session.add(gameItem3)
session.commit()

# Items for Football
game7 = Game(user_id=3, name="Football")

session.add(game7)
session.commit()


gameItem1 = GameItem(user_id=3, name="Football boot", description="Football b"
                     "oots, called cleats or soccer shoes in North America,[1"
                     "] are an item of footwear worn when playing football. T"
                     "hose designed for grass pitches have studs on the outso"
                     "le to aid grip.", game=game7)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=3, name="Ball", description="A football is a bal"
                     "l inflated with air that is used to play one of the var"
                     "ious sports known as football. In these games, with som"
                     "e exceptions, goals or points are scored only when the "
                     "ball enters one of two designated goal-scoring areas; f"
                     "ootball games involve the two teams each trying to move"
                     " the ball in opposite directions along the field of pla"
                     "y.", game=game7)

session.add(gameItem2)
session.commit()

# Items for Figure skating
game8 = Game(user_id=1, name="Figure skating")

session.add(game8)
session.commit()

gameItem1 = GameItem(user_id=1, name="Boots", description="Figure skating boo"
                     "ts are traditionally made by hand from many layers of l"
                     "eather. The design of figure skating boots changed sign"
                     "ificantly during the 20th century. Old photographs of s"
                     "katers such as Sonja Heine from the 1920s and 1930s sho"
                     "w them wearing thin, supple boots reaching to mid-calf.",
                     game=game8)

session.add(gameItem1)
session.commit()


gameItem2 = GameItem(user_id=1, name="Blades", description="Figure skates dif"
                     "fer most visibly from hockey skates in having a set of "
                     "large, jagged teeth called toe picks on the front of th"
                     "e blade. The toe picks are used primarily in jumping, f"
                     "ootwork and spins and should not be used for stroking. "
                     "Toe pick designs have become quite elaborate and someti"
                     "mes include additional picks on the sides of the blade,"
                     "often referred to as a k-pick.", game=game8)

session.add(gameItem2)
session.commit()

# Items for Ice Hockey
game9 = Game(user_id=2, name="Ice Hockey")

session.add(game9)
session.commit()

gameItem1 = GameItem(user_id=2, name="Hockey sticks", description="Made of wo"
                     "od or composite materials, hockey sticks come in variou"
                     "s styles and lengths. Stick dimensions vary based on th"
                     "e size of the player. Traditionally, all sticks were wo"
                     "oden up until the late 1990s; wood is inexpensive and t"
                     "ough, but the characteristics of each stick will be sub"
                     "tly different due to small changes in the grain structu"
                     "re. They also allow less flex before breaking.",
                     game=game9)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=2, name="Ice Skates", description="Hockey skates"
                     " incorporate a rigid shell, form-fit to the player's fo"
                     "ot using memory foam and/or heat-moldable components, o"
                     "ften reinforced with metal mesh to prevent a skate blad"
                     "e cutting through. Unlike figure skates, hockey skate b"
                     "lades have a rounded heel and no toe picks as these can"
                     " be dangerous in a \"pile-up\". Ice skates are essentia"
                     "l for all hockey players.", game=game9)

session.add(gameItem2)
session.commit()

# Items for Badminton
game10 = Game(user_id=3, name="Badminton")

session.add(game10)
session.commit()

gameItem1 = GameItem(user_id=3, name="Racket", description="A racket or racqu"
                     "et[1] is a sports implement consisting of a handled fra"
                     "me with an open hoop across which a network of strings "
                     "or catgut is stretched tightly. It is used for striking"
                     " a ball or shuttlecock in games such as squash, tennis,"
                     " racquetball, and badminton.", game=game10)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=3, name="Shuttlecock", description="A shuttlecoc"
                     "k (also called a bird or birdie) is a high-drag project"
                     "ile used in the sport of badminton. It has an open coni"
                     "cal shape formed by feathers (or a synthetic alternativ"
                     "e) embedded into a rounded cork (or rubber) base.",
                     game=game10)

session.add(gameItem2)
session.commit()
print "added menu items!"
