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
    {"username": "john_doe1", "email": "john_doe1@gmail.com"},
    {"username": "jane_smith2", "email": "jane_smith2@gmail.com"},
    {"username": "paul_brown3", "email": "paul_brown3@gmail.com"},
    {"username": "emily_davis4", "email": "emily_davis4@gmail.com"},
    {"username": "michael_jones5", "email": "michael_jones5@gmail.com"},
    {"username": "sarah_miller6", "email": "sarah_miller6@gmail.com"},
    {"username": "david_wilson7", "email": "david_wilson7@gmail.com"},
    {"username": "linda_moore8", "email": "linda_moore8@gmail.com"},
    {"username": "robert_taylor9", "email": "robert_taylor9@gmail.com"},
    {"username": "nancy_white10", "email": "nancy_white10@gmail.com"},
    {"username": "joshua_hall11", "email": "joshua_hall11@gmail.com"},
    {"username": "amanda_lewis12", "email": "amanda_lewis12@gmail.com"},
    {"username": "daniel_clark13", "email": "daniel_clark13@gmail.com"},
    {"username": "laura_robinson14", "email": "laura_robinson14@gmail.com"},
    {"username": "mark_harris15", "email": "mark_harris15@gmail.com"},
    {"username": "elizabeth_thomas16", "email": "elizabeth_thomas16@gmail.com"},
    {"username": "kevin_scott17", "email": "kevin_scott17@gmail.com"},
    {"username": "patricia_adams18", "email": "patricia_adams18@gmail.com"},
    {"username": "charles_evans19", "email": "charles_evans19@gmail.com"},
    {"username": "rebecca_martin20", "email": "rebecca_martin20@gmail.com"},
    {"username": "james_roberts21", "email": "james_roberts21@gmail.com"},
    {"username": "karen_mitchell22", "email": "karen_mitchell22@gmail.com"},
    {"username": "steven_carter23", "email": "steven_carter23@gmail.com"},
    {"username": "carolyn_wright24", "email": "carolyn_wright24@gmail.com"},
    {"username": "anthony_turner25", "email": "anthony_turner25@gmail.com"},
    {"username": "deborah_parker26", "email": "deborah_parker26@gmail.com"},
    {"username": "matthew_cooper27", "email": "matthew_cooper27@gmail.com"},
    {"username": "susan_anderson28", "email": "susan_anderson28@gmail.com"},
    {"username": "andrew_nguyen29", "email": "andrew_nguyen29@gmail.com"},
    {"username": "anna_hughes30", "email": "anna_hughes30@gmail.com"},
    {"username": "peter_king31", "email": "peter_king31@gmail.com"},
    {"username": "diane_bell32", "email": "diane_bell32@gmail.com"},
    {"username": "chris_wood33", "email": "chris_wood33@gmail.com"},
    {"username": "melissa_price34", "email": "melissa_price34@gmail.com"},
    {"username": "thomas_baker35", "email": "thomas_baker35@gmail.com"},
    {"username": "ryan_adams36", "email": "ryan_adams36@gmail.com"},
    {"username": "jessica_campbell37", "email": "jessica_campbell37@gmail.com"},
    {"username": "justin_morgan38", "email": "justin_morgan38@gmail.com"},
    {"username": "olivia_ross39", "email": "olivia_ross39@gmail.com"},
    {"username": "tyler_brooks40", "email": "tyler_brooks40@gmail.com"},
    {"username": "lauren_chen41", "email": "lauren_chen41@gmail.com"},
    {"username": "nathan_powell42", "email": "nathan_powell42@gmail.com"},
    {"username": "samantha_perry43", "email": "samantha_perry43@gmail.com"},
    {"username": "eric_reed44", "email": "eric_reed44@gmail.com"},
    {"username": "rachel_cook45", "email": "rachel_cook45@gmail.com"},
    {"username": "brandon_jenkins46", "email": "brandon_jenkins46@gmail.com"},
    {"username": "victoria_gray47", "email": "victoria_gray47@gmail.com"},
    {"username": "alex_howard48", "email": "alex_howard48@gmail.com"},
    {"username": "katherine_ward49", "email": "katherine_ward49@gmail.com"},
    {"username": "timothy_foster50", "email": "timothy_foster50@gmail.com"},
    {"username": "jennifer_rivera51", "email": "jennifer_rivera51@gmail.com"},
    {"username": "aaron_long52", "email": "aaron_long52@gmail.com"},
    {"username": "maria_torres53", "email": "maria_torres53@gmail.com"},
    {"username": "brian_peterson54", "email": "brian_peterson54@gmail.com"},
    {"username": "nicole_simmons55", "email": "nicole_simmons55@gmail.com"},
    {"username": "jason_russell56", "email": "jason_russell56@gmail.com"},
    {"username": "hannah_diaz57", "email": "hannah_diaz57@gmail.com"},
    {"username": "patrick_hayes58", "email": "patrick_hayes58@gmail.com"},
    {"username": "kelly_myers59", "email": "kelly_myers59@gmail.com"},
    {"username": "sean_ford60", "email": "sean_ford60@gmail.com"},
    {"username": "stephanie_hamilton61", "email": "stephanie_hamilton61@gmail.com"},
    {"username": "adam_graham62", "email": "adam_graham62@gmail.com"},
    {"username": "heather_sullivan63", "email": "heather_sullivan63@gmail.com"},
    {"username": "zachary_wallace64", "email": "zachary_wallace64@gmail.com"},
    {"username": "danielle_woods65", "email": "danielle_woods65@gmail.com"},
    {"username": "gregory_cole66", "email": "gregory_cole66@gmail.com"},
    {"username": "michelle_west67", "email": "michelle_west67@gmail.com"},
    {"username": "kyle_jordan68", "email": "kyle_jordan68@gmail.com"},
    {"username": "christina_owens69", "email": "christina_owens69@gmail.com"},
    {"username": "jeffrey_reynolds70", "email": "jeffrey_reynolds70@gmail.com"},
    {"username": "andrea_fisher71", "email": "andrea_fisher71@gmail.com"},
    {"username": "jose_ellis72", "email": "jose_ellis72@gmail.com"},
    {"username": "kimberly_harrison73", "email": "kimberly_harrison73@gmail.com"},
    {"username": "derek_gibson74", "email": "derek_gibson74@gmail.com"},
    {"username": "amy_mcdonald75", "email": "amy_mcdonald75@gmail.com"},
    {"username": "scott_cruz76", "email": "scott_cruz76@gmail.com"},
    {"username": "brittany_marshall77", "email": "brittany_marshall77@gmail.com"},
    {"username": "ian_ortiz78", "email": "ian_ortiz78@gmail.com"},
    {"username": "catherine_gomez79", "email": "catherine_gomez79@gmail.com"},
    {"username": "marcus_sullivan80", "email": "marcus_sullivan80@gmail.com"},
    {"username": "julia_mendoza81", "email": "julia_mendoza81@gmail.com"},
    {"username": "jordan_moreno82", "email": "jordan_moreno82@gmail.com"},
    {"username": "angela_fleming83", "email": "angela_fleming83@gmail.com"},
    {"username": "gabriel_walsh84", "email": "gabriel_walsh84@gmail.com"},
    {"username": "monica_watts85", "email": "monica_watts85@gmail.com"},
    {"username": "cody_silva86", "email": "cody_silva86@gmail.com"},
    {"username": "allison_vargas87", "email": "allison_vargas87@gmail.com"},
    {"username": "raymond_lynch88", "email": "raymond_lynch88@gmail.com"},
    {"username": "sabrina_hanson89", "email": "sabrina_hanson89@gmail.com"},
    {"username": "vincent_gardner90", "email": "vincent_gardner90@gmail.com"},
    {"username": "holly_weber91", "email": "holly_weber91@gmail.com"},
    {"username": "shane_bishop92", "email": "shane_bishop92@gmail.com"},
    {"username": "valerie_cortez93", "email": "valerie_cortez93@gmail.com"},
    {"username": "trevor_larson94", "email": "trevor_larson94@gmail.com"},
    {"username": "jill_bowen95", "email": "jill_bowen95@gmail.com"},
    {"username": "darren_schwartz96", "email": "darren_schwartz96@gmail.com"},
    {"username": "kristen_lamb97", "email": "kristen_lamb97@gmail.com"},
    {"username": "brett_hoffman98", "email": "brett_hoffman98@gmail.com"},
    {"username": "tara_manning99", "email": "tara_manning99@gmail.com"},
    {"username": "jared_hicks100", "email": "jared_hicks100@gmail.com"},
    {"username": "natalie_parks101", "email": "natalie_parks101@gmail.com"},
    {"username": "curtis_ryan102", "email": "curtis_ryan102@gmail.com"},
    {"username": "shannon_yates103", "email": "shannon_yates103@gmail.com"},
    {"username": "tony_francis104", "email": "tony_francis104@gmail.com"},
    {"username": "meghan_becker105", "email": "meghan_becker105@gmail.com"},
    {"username": "craig_oconnor106", "email": "craig_oconnor106@gmail.com"},
    {"username": "melanie_wade107", "email": "melanie_wade107@gmail.com"},
    {"username": "carlos_malone108", "email": "carlos_malone108@gmail.com"},
    {"username": "courtney_leonard109", "email": "courtney_leonard109@gmail.com"},
    {"username": "lance_deleon110", "email": "lance_deleon110@gmail.com"},
    {"username": "brooke_mcdaniel111", "email": "brooke_mcdaniel111@gmail.com"},
    {"username": "jeremiah_horton112", "email": "jeremiah_horton112@gmail.com"},
    {"username": "wendy_hodges113", "email": "wendy_hodges113@gmail.com"},
    {"username": "marc_zimmerman114", "email": "marc_zimmerman114@gmail.com"},
    {"username": "brenda_harrington115", "email": "brenda_harrington115@gmail.com"},
    {"username": "fernando_rhodes116", "email": "fernando_rhodes116@gmail.com"},
    {"username": "tracy_mccarthy117", "email": "tracy_mccarthy117@gmail.com"},
    {"username": "xavier_bridges118", "email": "xavier_bridges118@gmail.com"},
    {"username": "christine_griffith119", "email": "christine_griffith119@gmail.com"},
    {"username": "kent_burgess120", "email": "kent_burgess120@gmail.com"},
    {"username": "kristina_walls121", "email": "kristina_walls121@gmail.com"},
    {"username": "grant_acosta122", "email": "grant_acosta122@gmail.com"},
    {"username": "alicia_conway123", "email": "alicia_conway123@gmail.com"},
    {"username": "jonathon_stone124", "email": "jonathon_stone124@gmail.com"},
    {"username": "regina_olson125", "email": "regina_olson125@gmail.com"},
    {"username": "dustin_tran126", "email": "dustin_tran126@gmail.com"},
    {"username": "stacy_vaughn127", "email": "stacy_vaughn127@gmail.com"},
    {"username": "brad_richard128", "email": "brad_richard128@gmail.com"},
    {"username": "claire_hardy129", "email": "claire_hardy129@gmail.com"},
    {"username": "alan_farrell130", "email": "alan_farrell130@gmail.com"},
    {"username": "chelsea_wilkins131", "email": "chelsea_wilkins131@gmail.com"},
    {"username": "terry_norman132", "email": "terry_norman132@gmail.com"},
    {"username": "dana_moss133", "email": "dana_moss133@gmail.com"},
    {"username": "leo_wagner134", "email": "leo_wagner134@gmail.com"},
    {"username": "crystal_keller135", "email": "crystal_keller135@gmail.com"}
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


from datetime import datetime, timedelta

def populate_data():
    db = next(get_db())

    try:
        customer_objects = []  # Store customer objects separately

        for customer in customers:
            username = customer["username"]
            email = customer["email"]
            location = random.choice(rwanda_districts)
            password = f"password_{username}"
            hashed_password = pwd_context.hash(password)

            new_customer = Customer(
                username=username,
                email=email,
                location=location,
                hashed_password=hashed_password,
            )
            customer_objects.append(new_customer)
            print(new_customer.email)

        db.add_all(customer_objects)
        db.commit()

        # Fetch all customers from the database
        all_customers = db.query(Customer).all()

        # Generate 11405 orders with random or specific dates
        orders = []
        start_date = datetime(2024, 1, 1)  # Set the starting date
        end_date = datetime(2025, 2, 28)  # Set the ending date

        for _ in range(15105):
            customer = random.choice(all_customers)
            menu = random.choice(menu_items)

            # Randomly generate a date within the range
            random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

            order = Order(
                customer_id=customer.id,
                menu_name=menu["menu_name"],
                menu_details=menu["menu_details"],
                price=menu["price"],
                date=random_date,  # Set the specific/random date
            )
            orders.append(order)
            print(f"Order: {order.menu_name} | Date: {order.date}")

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
