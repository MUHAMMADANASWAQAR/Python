from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional, List
from datetime import datetime

# ============================================
# 1. BASIC MODEL
# ============================================
class Person(BaseModel):
    name: str
    age: int
    email: str

# Create and use basic model
person1 = Person(name="Ali", age=25, email="ali@example.com")
print("1. Basic Model:")
print(person1)
print()


# ============================================
# 2. FIELD VALIDATION AND CONSTRAINTS
# ============================================
class Student(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)  # ... means required
    age: int = Field(..., ge=5, le=100)  # ge=greater or equal, le=less or equal
    gpa: float = Field(..., ge=0.0, le=4.0)
    student_id: int = Field(..., gt=0)  # gt=greater than

# Create student with validation
student1 = Student(name="Hassan", age=20, gpa=3.8, student_id=101)
print("2. Field Validation:")
print(student1)
print()


# ============================================
# 3. OPTIONAL FIELDS AND DEFAULT VALUES
# ============================================
class User(BaseModel):
    username: str
    password: str
    phone: Optional[str] = None  # Optional - can be None
    is_active: bool = True  # Default value
    created_at: datetime = Field(default_factory=datetime.now)

user1 = User(username="john_doe", password="secure123")
print("3. Optional Fields & Defaults:")
print(user1)
print()


# ============================================
# 4. NESTED MODELS
# ============================================
class Address(BaseModel):
    street: str
    city: str
    country: str
    postal_code: str

class Employee(BaseModel):
    name: str
    salary: float
    address: Address  # Nested model

address = Address(street="123 Main St", city="Lahore", country="Pakistan", postal_code="54000")
employee = Employee(name="Sara", salary=50000, address=address)
print("4. Nested Models:")
print(employee)
print()


# ============================================
# 5. LISTS AND COLLECTIONS
# ============================================
class Team(BaseModel):
    team_name: str
    members: List[str]
    projects: List[str] = []  # Default empty list

team = Team(team_name="Dev Team", members=["Ali", "Sara", "Hassan"], projects=["ProjectA", "ProjectB"])
print("5. Lists:")
print(team)
print()


# ============================================
# 6. CUSTOM VALIDATORS
# ============================================
class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @validator('price')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Price must be greater than zero')
        return v

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if len(v.strip()) == 0:
            raise ValueError('Name cannot be empty')
        return v.strip()

product = Product(name="Laptop", price=50000, quantity=5)
print("6. Custom Validators:")
print(product)
print()


# ============================================
# 7. MODEL METHODS
# ============================================
class Rectangle(BaseModel):
    width: float
    height: float

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(width=10, height=5)
print("7. Model Methods:")
print(f"Width: {rect.width}, Height: {rect.height}")
print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")
print()


# ============================================
# 8. JSON SERIALIZATION (MODEL TO JSON)
# ============================================
class Course(BaseModel):
    course_id: int
    title: str
    instructor: str
    students_count: int

course = Course(course_id=101, title="Python Basics", instructor="Mr. Ahmed", students_count=30)
print("8. JSON Serialization:")
print("Model to Dict:", course.dict())
print("Model to JSON:", course.json())
print()


# ============================================
# 9. JSON DESERIALIZATION (JSON TO MODEL)
# ============================================
json_data = '{"course_id": 102, "title": "Advanced Python", "instructor": "Mr. Hassan", "students_count": 25}'
course2 = Course.parse_raw(json_data)
print("9. JSON Deserialization:")
print(course2)
print()


# ============================================
# 10. ERROR HANDLING
# ============================================
print("10. Error Handling:")
try:
    invalid_student = Student(name="ab", age=150, gpa=5.0, student_id=-5)
except Exception as e:
    print("Validation Error caught:")
    print(e)
print()


# ============================================
# 11. CONFIG CLASS (ADVANCED)
# ============================================
class ConfiguredModel(BaseModel):
    name: str
    age: int

    class Config:
        validate_assignment = True  # Validate on assignment
        arbitrary_types_allowed = True

model = ConfiguredModel(name="Ali", age=25)
print("11. Model Config:")
print(model)
print()


# ============================================
# 12. COMPUTED FIELDS / PROPERTIES
# ============================================
class Person_Full(BaseModel):
    first_name: str
    last_name: str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

person_full = Person_Full(first_name="Muhammad", last_name="Ali")
print("12. Computed Properties:")
print(f"Full Name: {person_full.full_name}")
print()


# ============================================
# 13. INHERITANCE
# ============================================
class BaseEntity(BaseModel):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)

class BlogPost(BaseEntity):
    title: str
    content: str
    author: str

post = BlogPost(id=1, title="Python Tips", content="Learn Python quickly", author="Ali")
print("13. Model Inheritance:")
print(post)
print()


# ============================================
# 14. MULTIPLE VALIDATORS
# ============================================
class StrictUser(BaseModel):
    username: str
    password: str
    email: str

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'Username must be alphanumeric'
        return v

    @validator('password')
    def password_min_length(cls, v):
        assert len(v) >= 8, 'Password must be at least 8 characters'
        return v

user_strict = StrictUser(username="john123", password="securepass123", email="john@example.com")
print("14. Multiple Validators:")
print(user_strict)
print()


# ============================================
# 15. SUMMARY OF KEY CONCEPTS
# ============================================
print("=" * 50)
print("PYDANTIC SUMMARY - KEY CONCEPTS:")
print("=" * 50)
print("""
1. BaseModel - Base class for all Pydantic models
2. Type Hints - Automatic type validation
3. Field() - Advanced field configuration
4. Validators - Custom validation logic
5. Optional[T] - Fields that can be None
6. List[T] - Collections with type safety
7. Nested Models - Compose models together
8. JSON Methods - dict(), json(), parse_raw()
9. Config Class - Model-level configuration
10. Inheritance - Extend existing models
11. Error Handling - ValidationError exceptions
12. @property - Computed fields
13. Custom Validators - @validator decorator
14. Default Values - Required vs optional fields
15. Model Methods - Add functionality to models
""")
