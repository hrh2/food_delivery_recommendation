from database import engine, Customer, Order

rwanda_districts = [
    "Nyarugenge", "Gasabo", "Kicukiro",  # City of Kigali
    "Burera", "Gakenke", "Gicumbi", "Musanze", "Rulindo",  # Northern Province
    "Gisagara", "Huye", "Kamonyi", "Muhanga", "Nyamagabe", "Nyanza", "Nyaruguru", "Ruhango",  # Southern Province
    "Bugesera", "Gatsibo", "Kayonza", "Kirehe", "Ngoma", "Nyagatare", "Rwamagana",  # Eastern Province
    "Karongi", "Ngororero", "Nyabihu", "Nyamasheke", "Rubavu", "Rusizi", "Rutsiro"  # Western Province
]

menu_items = [
    {"menu_name": "Grilled Chicken", "menu_details": "Tender grilled chicken with spices", "price": 7000},
    {"menu_name": "Beef Brochette", "menu_details": "Skewered beef chunks with vegetables", "price": 4500},
    {"menu_name": "Vegetable Pizza", "menu_details": "Cheesy pizza with fresh vegetables", "price": 8500},
    {"menu_name": "Spaghetti Bolognese", "menu_details": "Pasta with beef bolognese sauce", "price": 6500},
    {"menu_name": "Avocado Salad", "menu_details": "Fresh salad with avocado slices", "price": 4000},
    {"menu_name": "Fish and Chips", "menu_details": "Crispy fried fish with potato chips", "price": 9000},
    {"menu_name": "Chapati Rolls", "menu_details": "Stuffed chapati with veggies and meat", "price": 3500},
    {"menu_name": "Goat Stew", "menu_details": "Slow-cooked goat meat in tomato sauce", "price": 6000},
    {"menu_name": "Banana Smoothie", "menu_details": "Fresh banana smoothie with milk", "price": 2500},
    {"menu_name": "Egg Curry", "menu_details": "Boiled eggs in rich curry sauce", "price": 5000},
    {"menu_name": "Vegetable Samosas", "menu_details": "Fried pastries stuffed with veggies", "price": 2000},
    {"menu_name": "Rice Pilaf", "menu_details": "Rice cooked with spices and vegetables", "price": 5000},
    {"menu_name": "Fried Plantains", "menu_details": "Crispy fried ripe plantains", "price": 3500},
    {"menu_name": "Grilled Tilapia", "menu_details": "Whole grilled tilapia with herbs", "price": 11000},
    {"menu_name": "Chicken Curry", "menu_details": "Chicken in creamy curry sauce", "price": 8000},
    {"menu_name": "Hotdog", "menu_details": "Classic hotdog with mustard and ketchup", "price": 3000},
    {"menu_name": "Beef Burger", "menu_details": "Juicy beef patty with cheese and veggies", "price": 7000},
    {"menu_name": "Cheese Sandwich", "menu_details": "Toasted sandwich with melted cheese", "price": 4000},
    {"menu_name": "Fruit Salad", "menu_details": "Assorted seasonal fruits", "price": 3000},
    {"menu_name": "Beef Sausage", "menu_details": "Grilled beef sausage with sides", "price": 3500},
    {"menu_name": "Masala Tea", "menu_details": "Indian spiced milk tea", "price": 2000},
    {"menu_name": "Boiled Cassava", "menu_details": "Soft boiled cassava with a dipping sauce", "price": 2500},
    {"menu_name": "Tilapia Brochette", "menu_details": "Skewered tilapia chunks with spices", "price": 6000},
    {"menu_name": "Veggie Wrap", "menu_details": "Wrap filled with fresh vegetables", "price": 4000},
    {"menu_name": "Pilau", "menu_details": "East African spiced rice with meat", "price": 7000},
    {"menu_name": "Mandazi", "menu_details": "Soft and fluffy fried dough", "price": 1500},
    {"menu_name": "Chicken Wings", "menu_details": "Spicy and crispy chicken wings", "price": 5000},
    {"menu_name": "Meatballs", "menu_details": "Juicy meatballs in tomato sauce", "price": 6000},
    {"menu_name": "Ice Cream", "menu_details": "Vanilla and chocolate scoops", "price": 3000},
    {"menu_name": "Cappuccino", "menu_details": "Freshly brewed coffee with milk foam", "price": 2500},
    {"menu_name": "Beef Curry", "menu_details": "Tender beef in spicy curry sauce", "price": 7500},
    {"menu_name": "Spinach Lasagna", "menu_details": "Layers of pasta, spinach, and cheese", "price": 9500},
    {"menu_name": "Peanut Soup", "menu_details": "Rich soup made with ground peanuts", "price": 4000},
    {"menu_name": "Fried Rice", "menu_details": "Rice stir-fried with vegetables", "price": 5500},
    {"menu_name": "Chicken Brochette", "menu_details": "Skewered chicken chunks with peppers", "price": 5000},
    {"menu_name": "Vegetable Stir-Fry", "menu_details": "Mixed veggies stir-fried with soy sauce", "price": 4500},
    {"menu_name": "Mango Juice", "menu_details": "Freshly squeezed mango juice", "price": 2500},
    {"menu_name": "Boiled Potatoes", "menu_details": "Boiled potatoes with parsley", "price": 3000},
    {"menu_name": "Chicken Fried Rice", "menu_details": "Rice stir-fried with chicken and veggies", "price": 7000},
    {"menu_name": "Beef Sandwich", "menu_details": "Grilled beef slices in fresh bread", "price": 6000},
    {"menu_name": "Cassava Leaves", "menu_details": "Stewed cassava leaves with peanut sauce", "price": 5000},
    {"menu_name": "Ginger Tea", "menu_details": "Hot tea infused with fresh ginger", "price": 1500},
    {"menu_name": "Passion Fruit Juice", "menu_details": "Sweet and tangy juice", "price": 2500},
    {"menu_name": "Avocado Toast", "menu_details": "Toasted bread topped with avocado", "price": 4000},
    {"menu_name": "Beef Stew", "menu_details": "Beef cooked with vegetables and spices", "price": 8000},
    {"menu_name": "Chocolate Cake", "menu_details": "Rich chocolate dessert", "price": 5500},
    {"menu_name": "Omelette", "menu_details": "Fluffy eggs with veggies", "price": 3500},
    {"menu_name": "Rwandan Coffee", "menu_details": "Freshly brewed Rwandan coffee", "price": 3000},
    {"menu_name": "Meat Pie", "menu_details": "Flaky pastry filled with minced meat", "price": 4000}
]

customers = [
    {"username": "john_doe1", "email": "john_doe1@example.com"},
    {"username": "jane_smith2", "email": "jane_smith2@example.com"},
    {"username": "paul_brown3", "email": "paul_brown3@example.com"},
    {"username": "emily_davis4", "email": "emily_davis4@example.com"},
    {"username": "michael_jones5", "email": "michael_jones5@example.com"},
    {"username": "sarah_miller6", "email": "sarah_miller6@example.com"},
    {"username": "david_wilson7", "email": "david_wilson7@example.com"},
    {"username": "linda_moore8", "email": "linda_moore8@example.com"},
    {"username": "robert_taylor9", "email": "robert_taylor9@example.com"},
    {"username": "nancy_white10", "email": "nancy_white10@example.com"},
    {"username": "joshua_hall11", "email": "joshua_hall11@example.com"},
    {"username": "amanda_lewis12", "email": "amanda_lewis12@example.com"},
    {"username": "daniel_clark13", "email": "daniel_clark13@example.com"},
    {"username": "laura_robinson14", "email": "laura_robinson14@example.com"},
    {"username": "mark_harris15", "email": "mark_harris15@example.com"},
    {"username": "elizabeth_thomas16", "email": "elizabeth_thomas16@example.com"},
    {"username": "kevin_scott17", "email": "kevin_scott17@example.com"},
    {"username": "patricia_adams18", "email": "patricia_adams18@example.com"},
    {"username": "charles_evans19", "email": "charles_evans19@example.com"},
    {"username": "rebecca_martin20", "email": "rebecca_martin20@example.com"},
    {"username": "james_roberts21", "email": "james_roberts21@example.com"},
    {"username": "karen_mitchell22", "email": "karen_mitchell22@example.com"},
    {"username": "steven_carter23", "email": "steven_carter23@example.com"},
    {"username": "carolyn_wright24", "email": "carolyn_wright24@example.com"},
    {"username": "anthony_turner25", "email": "anthony_turner25@example.com"},
    {"username": "deborah_parker26", "email": "deborah_parker26@example.com"},
    {"username": "matthew_cooper27", "email": "matthew_cooper27@example.com"},
    {"username": "susan_anderson28", "email": "susan_anderson28@example.com"},
    {"username": "andrew_nguyen29", "email": "andrew_nguyen29@example.com"},
    {"username": "anna_hughes30", "email": "anna_hughes30@example.com"},
    {"username": "peter_king31", "email": "peter_king31@example.com"},
    {"username": "diane_bell32", "email": "diane_bell32@example.com"},
    {"username": "chris_wood33", "email": "chris_wood33@example.com"},
    {"username": "melissa_price34", "email": "melissa_price34@example.com"},
    {"username": "thomas_baker35", "email": "thomas_baker35@example.com"}
]


import random
from sqlalchemy.orm import Session
from passlib.context import CryptContext


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database session
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

# Generate 5000 unique customers and 11405 orders
def populate_data():
    db = next(get_db())

    try:
        # Generate 5000 unique customers
        customers = []
        for i in range(5000):
            username = f"user_{i+1}"
            email = f"user_{i+1}@example.com"
            location = random.choice(rwanda_districts)
            password = f"password_{i+1}"
            hashed_password = pwd_context.hash(password)

            customer = Customer(
                username=username,
                email=email,
                location=location,
                hashed_password=hashed_password,
            )
            customers.append(customer)
            print(customer.email)

        db.add_all(customers)
        db.commit()

        # Fetch all customers from the database
        all_customers = db.query(Customer).all()

        # Generate 11405 orders
        orders = []
        for _ in range(11405):
            customer = random.choice(all_customers)
            menu = random.choice(menu_items)

            order = Order(
                customer_id=customer.id,
                menu_name=menu["menu_name"],
                menu_details=menu["menu_details"],
                price=menu["price"],
            )
            orders.append(order)
            print(order.menu_name)

        db.add_all(orders)
        db.commit()

        print("Data populated successfully!")
    except Exception as e:
        db.rollback()
        print("An error occurred:", e)
    finally:
        db.close()

# Run the script
if __name__ == "__main__":
    populate_data()
