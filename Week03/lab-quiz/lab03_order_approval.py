try:
    order_amount = float(input("Sipariş tutarını girin (TRY): "))
    available_stock = int(input("Mevcut stok miktarını girin: "))
    requested_qty = int(input("Talep edilen ürün adedini girin: "))
    is_member_input = input("Müşteri üye mi? (e/h): ").strip().lower()
    is_member = is_member_input in ['e', 'evet', 'yes', 'y']

    if requested_qty <= 0 or order_amount <= 0:
        print("Sipariş Reddedildi: Geçersiz ürün adedi veya tutar girdiniz.")
    elif requested_qty > available_stock:
        print("Sipariş Reddedildi: Yetersiz stok.")
    else:
        discount = 0.0
        if is_member and order_amount >= 500:
            discount = 0.10
            final_price = order_amount * (1 - discount)
            print("Sipariş Onaylandı: Stok yeterli. Üyelere özel 500 TRY üzeri %10 indirim uygulandı!")
            print(f"Ödenecek Son Tutar: {final_price:.2f} TRY")
        else:
            final_price = order_amount
            print("Sipariş Onaylandı: Stok yeterli.")
            print(f"Ödenecek Son Tutar: {final_price:.2f} TRY")

except ValueError:
    print("Hatalı giriş yaptınız. Lütfen sayısal değerleri doğru girin.")
