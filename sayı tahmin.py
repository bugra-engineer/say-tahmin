import random


def sayi_tahmin_oyunu():
    hedef_sayi = random.randint(1, 100)
    deneme_sayisi = 0

    print("=== SAYI TAHMİN OYUNU ===")
    print("1 ile 100 arasında bir sayı tuttum. Tahmin etmeye çalış!\n")

    while True:
        try:
            tahmin = int(input("Tahmininiz: "))
            deneme_sayisi += 1

            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
                continue

            if tahmin < hedef_sayi:
                print("Daha büyük bir sayı girin ⬆️")
            elif tahmin > hedef_sayi:
                print("Daha küçük bir sayı girin ⬇️")
            else:
                print(
                    f"\nTebrikler! {hedef_sayi} sayısını {deneme_sayisi} denemede buldunuz! 🎉"
                )
                break
        except ValueError:
            print("Geçersiz giriş! Lütfen sadece tam sayı girin.")


if __name__ == "__main__":
    sayi_tahmin_oyunu()