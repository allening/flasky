import sqlalchemy
print sqlalchemy.__version__




# from sqlalchemy import ForeignKey
# from sqlalchemy import relationship

# class Address(Base):
#     __tablenname__ = 'addresses'
#     id = Column(Integer, primary_key=True)
#     email_address = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'))