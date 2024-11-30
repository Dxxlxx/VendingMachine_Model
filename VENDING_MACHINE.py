# ฟังก์ชันสำหรับการแสดงเมนูเครื่องดื่ม
def display_menu(language):
    if language == "ไทย":
        print("\nเมนูเครื่องดื่ม:")
        print("1. กาแฟ - 40 บาท")
        print("2. ชาเขียว - 50 บาท")
        print("3. นมสด - 30 บาท")
        print("4. น้ำส้ม - 35 บาท")
    else:
        print("\nDrink Menu:")
        print("1. Coffee - 40 Baht")
        print("2. Green Tea - 50 Baht")
        print("3. Fresh Milk - 30 Baht")
        print("4. Orange Juice - 35 Baht")

# ฟังก์ชันการเลือกปรับแต่งเมนู
def customize_drink(language):
    if language == "ไทย":
        print("\nตัวเลือกปรับแต่ง:")
        print("1. ระดับความหวาน: ไม่หวาน / หวานน้อย / หวานปกติ")
        print("2. ปริมาณน้ำแข็ง: ไม่ใส่น้ำแข็ง / น้อย / ปกติ / มาก")
    else:
        print("\nCustomization Options:")
        print("1. Sweetness level: Unsweetened / Less Sweet / Normal")
        print("2. Ice level: No Ice / Less Ice / Normal / Extra Ice")

    sweetness = input("\nChoose sweetness level (1, 2, or 3): ")
    ice_level = input("Choose ice level (1, 2, 3, or 4): ")

    return sweetness, ice_level

# ฟังก์ชันการชำระเงิน (รองรับเงินสดและ e-Wallet)
def process_payment(price, language):
    print("\nPayment Methods:")
    print("1. Cash")
    print("2. e-Wallet (QR Code)")

    payment_method = input("Choose your payment method (1 or 2): ")
    if payment_method == "1":
        return process_cash_payment(price, language)
    elif payment_method == "2":
        if language == "ไทย":
            print("กรุณาสแกน QR Code เพื่อชำระเงิน")
        else:
            print("Please scan the QR Code to complete payment")
        print("Payment successful!")
        return True
    else:
        if language == "ไทย":
            print("วิธีการชำระเงินไม่ถูกต้อง")
        else:
            print("Invalid payment method")
        return False

# ฟังก์ชันการชำระเงินด้วยเงินสด
def process_cash_payment(price, language):
    while True:
        try:
            if language == "ไทย":
                amount = float(input(f"กรุณาใส่จำนวนเงิน ({price} บาท): "))
            else:
                amount = float(input(f"Please insert payment ({price} Baht): "))
            
            if amount < price:
                if language == "ไทย":
                    print(f"จำนวนเงินไม่พอ ขาดอีก {price - amount} บาท")
                else:
                    print(f"Insufficient amount. You need {price - amount} more Baht.")
            else:
                change = amount - price
                if change > 0:
                    if language == "ไทย":
                        print(f"เงินทอนของคุณคือ {change:.2f} บาท")
                    else:
                        print(f"Your change is {change:.2f} Baht.")
                return True
        except ValueError:
            if language == "ไทย":
                print("กรุณาใส่จำนวนเงินที่ถูกต้อง")
            else:
                print("Please enter a valid amount.")

# ฟังก์ชันสำหรับสมาชิกสะสมแต้ม
def member_system(language):
    if language == "ไทย":
        print("\nระบบสมาชิก: รับแต้มสะสมทุกการซื้อ!")
        member_id = input("กรุณาใส่หมายเลขสมาชิก (หรือกด Enter หากไม่มี): ")
    else:
        print("\nMembership System: Earn points on every purchase!")
        member_id = input("Please enter your membership ID (or press Enter if none): ")
    
    if member_id:
        if language == "ไทย":
            print(f"ยินดีต้อนรับ สมาชิกหมายเลข {member_id}! คุณได้รับ 1 แต้มสะสม")
        else:
            print(f"Welcome, Member ID {member_id}! You have earned 1 point.")
    else:
        if language == "ไทย":
            print("ขอบคุณที่ใช้บริการ!")
        else:
            print("Thank you for using our service!")

# ฟังก์ชันแสดงโปรโมชั่น
def show_promotions(language):
    if language == "ไทย":
        print("\nโปรโมชั่นพิเศษ:")
        print("1. ซื้อ 1 แก้ว แถม 1 แก้ว (เฉพาะวันนี้!)")
        print("2. สะสมครบ 10 แต้ม แลกรับเครื่องดื่มฟรี 1 แก้ว")
    else:
        print("\nSpecial Promotions:")
        print("1. Buy 1 Get 1 Free (Today Only!)")
        print("2. Earn 10 points to redeem 1 free drink!")

# ฟังก์ชันหลักของตู้กดน้ำ
def vending_machine():
    print("Welcome to the Smart Vending Machine!")
    print("กรุณาเลือกภาษา / Please select a language:")
    print("1. ภาษาไทย (Thai)")
    print("2. English")
    
    # เลือกภาษา
    language_choice = input("Enter your choice (1 or 2): ")
    if language_choice == "1":
        language = "ไทย"
    elif language_choice == "2":
        language = "English"
    else:
        print("Invalid choice. Defaulting to English.")
        language = "English"
    
    # แสดงโปรโมชั่น
    show_promotions(language)
    
    # แสดงเมนูเครื่องดื่ม
    display_menu(language)
    
    # รับการเลือกเครื่องดื่ม
    drink_choice = input("\nEnter your choice (1, 2, 3, or 4): ")
    
    # รายละเอียดเครื่องดื่ม
    drinks = {
        "1": {"name_th": "กาแฟ", "name_en": "Coffee", "price": 40},
        "2": {"name_th": "ชาเขียว", "name_en": "Green Tea", "price": 50},
        "3": {"name_th": "นมสด", "name_en": "Fresh Milk", "price": 30},
        "4": {"name_th": "น้ำส้ม", "name_en": "Orange Juice", "price": 35},
    }
    
    selected_drink = drinks.get(drink_choice)
    if not selected_drink:
        if language == "ไทย":
            print("ไม่พบเมนูที่เลือก")
        else:
            print("Invalid selection")
        return
    
    # แสดงเครื่องดื่มที่เลือก
    if language == "ไทย":
        print(f"คุณเลือก {selected_drink['name_th']} ราคา {selected_drink['price']} บาท")
    else:
        print(f"You selected {selected_drink['name_en']} costing {selected_drink['price']} Baht")
    
    # เลือกปรับแต่งเครื่องดื่ม
    customize_drink(language)
    
    # กระบวนการชำระเงิน
    if process_payment(selected_drink["price"], language):
        # ระบบสมาชิก
        member_system(language)

    print("Thank you!")

# เรียกใช้งานตู้กดน้ำ
vending_machine()