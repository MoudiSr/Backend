from rest_framework import serializers
from .models import Order, User, Employee, Expense

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('id', 'order_id', 'dealer_name', 'client_name', 'location', 'order_Dollar', 'order_LBP', 'delivery', 'delivery_currency', 'final_amount_LBP', 'final_amount_Dollar', 'driver_tax', 'driver_tax_Currency', 'remaining_amount_LBP', 'remaining_amount_Dollar', 'items', 'date', 'user', 'status')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'admin')

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = ('id', 'payment_id', 'name', 'payment', 'quantity', 'currency', 'date', 'user')

class ExpenseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Expense
		fields = ('id', 'payment_id', 'payment_type', 'amount_dollar', 'amount_lbp', 'date', 'user')