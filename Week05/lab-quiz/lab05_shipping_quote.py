def get_subtotal(price, qty):
    return price * qty

def get_discount(sub):
    return 0.15 if sub >= 1000 else 0.0

def get_shipping(sub):
    return 0.0 if sub >= 750 else 50.0

def get_total(sub, disc, ship):
    return (sub * (1 - disc)) + ship

s1 = get_subtotal(200, 2)
print("1. Sipariş Toplamı:", get_total(s1, get_discount(s1), get_shipping(s1)))

s2 = get_subtotal(350, 3)
print("2. Sipariş Toplamı:", get_total(s2, get_discount(s2), get_shipping(s2)))

assert get_subtotal(100, 4) == 400
assert get_discount(1000) == 0.15
assert get_total(500, 0.10, 50) == 500.0

print("Testler başarıyla geçti!")
