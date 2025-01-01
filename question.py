def ask_question():
 \xd9   print("ما هو لون السماء؟")
    print("1. أزرق")
    print("2. رمادي")
    
    choice = input("اختر رقم الخيار (1 أو 2): ")
    
    if choice == "1":
        print("صحيح! لون السماء في الأيام الصافية هو الأزرق.")
    elif choice == "2":
        print("خطأ! عادةً ما يكون لون السماء أزرق في الأيام الصافية.")
    else:
        print("اختيار غير صالح. يرجى اختيار 1 أو 2.")

if __name__ == "__main__":
    ask_question()
