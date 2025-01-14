import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Set up the database engine and session
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Define models
class DeviceCategory(Base):
    """description: Represents categories of devices like NAS, DAS, etc."""
    __tablename__ = 'device_category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)

class Product(Base):
    """description: Represents the different products available for sale."""
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('device_category.id'))
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)

class Accessory(Base):
    """description: Represents accessories for devices, such as cables and additional storage."""
    __tablename__ = 'accessory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

class Supplier(Base):
    """description: Represents suppliers providing products and accessories."""
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_info = Column(Text)

class Customer(Base):
    """description: Represents customers who purchase products and accessories."""
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String)

class Order(Base):
    """description: Represents orders made by customers."""
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    order_date = Column(DateTime, default=datetime.datetime.now)

class OrderItem(Base):
    """description: Represents individual items within an order."""
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)

class Inventory(Base):
    """description: Represents inventory details for each product."""
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    location = Column(String, nullable=False)
    quantity_on_hand = Column(Integer, nullable=False)

class SupplierProduct(Base):
    """description: Represents the products provided by each supplier."""
    __tablename__ = 'supplier_product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    product_id = Column(Integer, ForeignKey('product.id'))

class CategoryAttribute(Base):
    """description: Represents attributes specific to each device category."""
    __tablename__ = 'category_attribute'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('device_category.id'))
    attribute_name = Column(String, nullable=False)
    value = Column(String, nullable=False)

class Promotion(Base):
    """description: Represents promotions for products and accessories."""
    __tablename__ = 'promotion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

class Review(Base):
    """description: Represents customer reviews for products."""
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    rating = Column(Integer)
    comment = Column(Text)
    review_date = Column(DateTime, default=datetime.datetime.now)

# Create tables
Base.metadata.create_all(engine)

# Insert sample data
device_category1 = DeviceCategory(name="NAS", description="Network Attached Storage Devices")
device_category2 = DeviceCategory(name="DAS", description="Direct Attached Storage Devices")

product1 = Product(name="NAS Model A", category_id=1, price=299.99, stock_quantity=20)
product2 = Product(name="DAS Model B", category_id=2, price=199.99, stock_quantity=15)

accessory1 = Accessory(name="Cat-5 Ethernet Cable", description="High-speed Ethernet cable.", price=15.99, stock_quantity=100)
accessory2 = Accessory(name="USB-C Cable", description="USB-C cable for fast charging.", price=9.99, stock_quantity=200)

supplier1 = Supplier(name="Tech Supplies Corp", contact_info="email: techsupplies@example.com")
supplier2 = Supplier(name="Storage Distributors", contact_info="email: storagedistribute@example.com")

customer1 = Customer(first_name="John", last_name="Doe", email="john.doe@example.com", phone_number="1234567890")
customer2 = Customer(first_name="Jane", last_name="Smith", email="jane.smith@example.com", phone_number="0987654321")

order1 = Order(customer_id=1, order_date=datetime.datetime.now())

order_item1 = OrderItem(order_id=1, product_id=1, quantity=1, unit_price=299.99) 

inventory1 = Inventory(product_id=1, location="Warehouse 1", quantity_on_hand=50)

supplier_product1 = SupplierProduct(supplier_id=1, product_id=1)

category_attr1 = CategoryAttribute(category_id=1, attribute_name="Connectivity", value="Ethernet")

promotion1 = Promotion(name="Holiday Sale", description="Discount on all devices", start_date=datetime.datetime(2023, 11, 20), end_date=datetime.datetime(2023, 12, 31))

review1 = Review(customer_id=1, product_id=1, rating=5, comment="Great product!", review_date=datetime.datetime.now())

# Add all instances to the session
session.add_all([device_category1, device_category2, product1, product2, accessory1, accessory2,
                 supplier1, supplier2, customer1, customer2, order1, order_item1, inventory1,
                 supplier_product1, category_attr1, promotion1, review1])

# Commit the session
session.commit()

# Close the session
session.close()
