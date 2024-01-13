from db import Session, Group, Goods


with Session() as session:
    group = Group(name="Teddy")


    session.add(group)
    session.commit()