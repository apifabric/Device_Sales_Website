# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 12, 2024 14:38:59
# Database: sqlite:////tmp/tmp.hBRHx8Q3Mo/Device_Sales_Website/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Accessory(SAFRSBaseX, Base):
    """
    description: Represents accessories for devices, such as cables and additional storage.
    """
    __tablename__ = 'accessory'
    _s_collection_name = 'Accessory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Customer(SAFRSBaseX, Base):
    """
    description: Represents customers who purchase products and accessories.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="customer")



class DeviceCategory(SAFRSBaseX, Base):
    """
    description: Represents categories of devices like NAS, DAS, etc.
    """
    __tablename__ = 'device_category'
    _s_collection_name = 'DeviceCategory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    # parent relationships (access parent)

    # child relationships (access children)
    CategoryAttributeList : Mapped[List["CategoryAttribute"]] = relationship(back_populates="category")
    ProductList : Mapped[List["Product"]] = relationship(back_populates="category")



class Promotion(SAFRSBaseX, Base):
    """
    description: Represents promotions for products and accessories.
    """
    __tablename__ = 'promotion'
    _s_collection_name = 'Promotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Supplier(SAFRSBaseX, Base):
    """
    description: Represents suppliers providing products and accessories.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(Text)

    # parent relationships (access parent)

    # child relationships (access children)
    SupplierProductList : Mapped[List["SupplierProduct"]] = relationship(back_populates="supplier")



class CategoryAttribute(SAFRSBaseX, Base):
    """
    description: Represents attributes specific to each device category.
    """
    __tablename__ = 'category_attribute'
    _s_collection_name = 'CategoryAttribute'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    category_id = Column(ForeignKey('device_category.id'))
    attribute_name = Column(String, nullable=False)
    value = Column(String, nullable=False)

    # parent relationships (access parent)
    category : Mapped["DeviceCategory"] = relationship(back_populates=("CategoryAttributeList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Represents orders made by customers.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    order_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class Product(SAFRSBaseX, Base):
    """
    description: Represents the different products available for sale.
    """
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(ForeignKey('device_category.id'))
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime)

    # parent relationships (access parent)
    category : Mapped["DeviceCategory"] = relationship(back_populates=("ProductList"))

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="product")
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="product")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="product")
    SupplierProductList : Mapped[List["SupplierProduct"]] = relationship(back_populates="product")



class Inventory(SAFRSBaseX, Base):
    """
    description: Represents inventory details for each product.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'))
    location = Column(String, nullable=False)
    quantity_on_hand = Column(Integer, nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class OrderItem(SAFRSBaseX, Base):
    """
    description: Represents individual items within an order.
    """
    __tablename__ = 'order_item'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'))
    product_id = Column(ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)



class Review(SAFRSBaseX, Base):
    """
    description: Represents customer reviews for products.
    """
    __tablename__ = 'review'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    product_id = Column(ForeignKey('product.id'))
    rating = Column(Integer)
    comment = Column(Text)
    review_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("ReviewList"))
    product : Mapped["Product"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)



class SupplierProduct(SAFRSBaseX, Base):
    """
    description: Represents the products provided by each supplier.
    """
    __tablename__ = 'supplier_product'
    _s_collection_name = 'SupplierProduct'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(ForeignKey('supplier.id'))
    product_id = Column(ForeignKey('product.id'))

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("SupplierProductList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("SupplierProductList"))

    # child relationships (access children)
