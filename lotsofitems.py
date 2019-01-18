from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Clayton", email="clayton@gmail.com")
session.add(User1)
session.commit()

# Create category of Action Films
category1 = Categories(user_id=1, name="Action Films")
session.add(category1)
session.commit()


# Create category of Adventure Films
category2 = Categories(user_id=1, name="Adventure Films")
session.add(category2)
session.commit()

# Create category of Comedy Films
category3 = Categories(user_id=1, name="Comedy Films")
session.add(category3)
session.commit()

# Create category of Crime & Gangster Films
category4 = Categories(user_id=1, name="Crime & Gangster Films")
session.add(category4)
session.commit()

# Create category of Drama Films
category5 = Categories(user_id=1, name="Drama Films")
session.add(category5)
session.commit()

# Create category of Epics/Historical Films
category6 = Categories(user_id=1, name="Epics/Historical Films")
session.add(category6)
session.commit()

# Create category of Horror Films
category7 = Categories(user_id=1, name="Horror Films")
session.add(category7)
session.commit()

# Create category of Musicals (Dance) Films
category8 = Categories(user_id=1, name="Musicals (Dance) Films")
session.add(category8)
session.commit()

# Create category of Science Fiction Films
category9 = Categories(user_id=1, name="Science Fiction Films")
session.add(category9)
session.commit()

# Create category of War (Anti-War) Films
category10 = Categories(user_id=1, name="War (Anti-War) Films")
session.add(category10)
session.commit()

# Create category of Westerns
category11 = Categories(user_id=1, name="Westerns")
session.add(category11)
session.commit()


# Add Items into categories
categoryItem1 = CategoryItem(user_id=1, name="La La Land",
                             description="La La Land is a 2016 American romantic musical film written and directed by Damien Chazelle. It stars Ryan Gosling as a jazz pianist and Emma Stone as an aspiring actress, who meet and fall in love in Los Angeles while pursuing their dreams.",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Exorcism of Emily Rose",
                             description="The Exorcism of Emily Rose is a 2005 American supernatural horror trial film directed by Scott Derrickson and starring Laura Linney and Tom Wilkinson. The film is loosely based on the story of Anneliese Michel and follows a self-proclaimed agnostic (Linney) who acts as defense counsel representing a parish priest (Wilkinson), accused by the state of negligent homicide after he performed an exorcism.",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Das Boot",
                             description="An adaptation of Lothar-Gunther Buchheim's 1973 German novel of the same name, the film is set during World War II and follows German U-boat U-96 and its crew, as they set out on a hazardous patrol in the Battle of the Atlantic. It depicts both the excitement of battle and the tedium of the fruitless hunt, and shows the men serving aboard U-boats as ordinary individuals with a desire to do their best for their comrades and their country.",
                             categories=category10)
session.add(categoryItem1)
session.commit()



categoryItem1 = CategoryItem(user_id=1, name="Miller's Crossing",
                             description="Miller's Crossing is a 1990 American neo-noir gangster film written, directed and produced by the Coen brothers and starring Gabriel Byrne, Marcia Gay Harden, John Turturro, Jon Polito, J. E. Freeman, and Albert Finney. The plot concerns a power struggle between two rival gangs and how the protagonist, Tom Reagan (Byrne), plays both sides off against each other.",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Black Panther",
                             description="After his father's death, T'Challa returns home to Wakanda to inherit his throne. However, a powerful enemy related to his family threatens to attack his nation.",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Step Up",
                             description="Tyler and Nora meet at Maryland School of the Arts, where Tyler works as a janitor. They fall in love and encourage each other to follow their passion for dance and fulfil their dreams.",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Revenant",
                             description="Hugh Glass, a legendary frontiersman, is severely injured in a bear attack and is abandoned by his hunting crew. He uses his skills to survive and take revenge on his companion who betrayed him.",
                             categories=category11)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Social Network",
                             description="Mark Zuckerberg creates a social networking site, Facebook, with the help of his friend Eduardo Saverin. But soon, a string of lies tears their relationship apart even as Facebook connects people.",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Lincoln",
                             description="Abraham Lincoln uses his powers as the president of the United States of America as he strives to abolish slavery and reunite his country during the Civil War.",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Interstellar",
                             description="In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life.",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Terminator",
                             description="A cyborg assassin is sent back in time to kill Sarah, a waitress, in a bid to stop her son who will wage a long war against his enemy in the future unless the course of history is altered.",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="American Gangster",
                             description="James Kirk, a brash young man, and Spock, an alien with human and Vulcan blood, join the crew of the USS Enterprise to combat Nero, a member of the Romulan race who wants to destroy multiple planets.",
                             categories=category4)
session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Dunkirk",
                             description="Allied soldiers from Belgium, \
                             the British Empire and France are surrounded\
                              by the German Army, and evacuated during a \
                              fierce battle in World War II.",
                             categories=category5)
session.add(categoryItem1)
session.commit()



categoryItem1 = CategoryItem(user_id=1, name="Star Trek",
                             description="James Kirk, a brash young man, and Spock, an alien with human and Vulcan blood, join the crew of the USS Enterprise to combat Nero, a member of the Romulan race who wants to destroy multiple planets.",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Wonder Woman",
                             description="Princess Diana of an all-female Amazonian race rescues US pilot Steve. Upon learning of a war, she ventures into the world of men to stop Ares, the god of war, from destroying mankind.",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,
                             name="Bumblebee",
                             description="On the run in the year 1987, Bumblebee the Autobot seeks refuge in a junkyard in a small California beach town. Charlie, on the brink of turning 18 years old and trying to find her place in the world, soon discovers the battle-scarred and broken Bumblebee. ",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Conjuring",
                             description="Rod and Carolyn find their pet dog dead under mysterious circumstances and experience a spirit that harms their daughter Andrea. They finally call investigators who can help them get out of the mess.",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Dictator",
                             description="Aladeen, a dictator, travels to New York in order to address The United Nations Security Council. However, his plans get messed up when he gets kidnapped.",
                             categories=category3)
session.add(categoryItem1)
session.commit()

print "added category items!"
