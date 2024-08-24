import random 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Label to show messages
        self.label = Label(text="Bir şık seçin", font_size=24)
        layout.add_widget(self.label)

        # Buttons with different colors
        green_button = Button(text="Mutluysan Tıkla", background_color=(0, 1, 0, 1), font_size=24)
        blue_button = Button(text="Üzgünsen Tıkla ", background_color=(0, 0, 1, 1), font_size=24)
        red_button = Button(text="Gergin veya Sinirliysen Tıkla", background_color=(1, 0, 0, 1), font_size=24)

        # Bind buttons to functions
        green_button.bind(on_press=self.on_green_button_press)
        blue_button.bind(on_press=self.on_blue_button_press)
        red_button.bind(on_press=self.on_red_button_press)

        # Add buttons to the layout
        layout.add_widget(green_button)
        layout.add_widget(blue_button)
        layout.add_widget(red_button)

        return layout

    def on_green_button_press(self, instance): #Mutlu
        green_sentences = [
            "Her ne için mutlu oldun bilmiyorum ama bildiğim bir şey var, o da güldüğün zaman güzel görüneceğin."
            "Mutlu Olduğun zaman mutlu hisseden biri var şuan o kişi de çok mutlu :)"
            "Çoğu şarkılardan daha hoş gülüşün var şuan bunu göstermenin tam zamanı."
            "Bu şıkka tıkladığına göre şuan mutlusun hemen bunu sevdiklerinle paylaş. Sadece gülümsemen yeterli"
            "Gülümsediğin zaman kışta kavun, yazda çilek yetişir. Çünkü onlar da gülmek için illaki bir şeyler gerçekleşmemesi gerektiğini biliyor, just smile"
            "Hiçbir zaman seni mutlu edeni ve bunu sürdürmeni sağlayan kişiyi unutma çünkü onlar sana en çok değer verenlerdir."
        ]
        self.label.text = random.choice(green_sentences)

    def on_blue_button_press(self, instance): #Üzgün
        blue_sentences = [
            "Üzülme, bunlar da geçer. Hatırla neleri atlattık biz seninle...",
            "Seninle birlikte aşamadığımız hiçbir şey yok sadece sabretmeliyiz. Bana güvenebilirsin, benim sana güvendiğim gibi"
            "Senin zorluklara karşı çok yorulduğunu biliyorum en ufak olaylara üzülmeyeceğini biliyorum. Üzgünsen ciddi bir sebebi vardır, ama sen de unutma ki her şeyi aşabilirsin."
            "Bu zamana kadar neler aşmadık ki elbette çok zorlandık, yorulduk ama sonucunda bunu çözdük kendini üzmemelisin bir tanem yanında her zaman biri var."
            "Hey, Çok güzelsin ve üzgünken beni karışık duygulara sokuyorsun hem aşık oluyorum hem üzülüyorum. Bunu birlikte çözelim ve sorunu halledelim :)"
            "Seni Seviyorum. Sadece bil istedim."
        ]
        self.label.text = random.choice(blue_sentences)

    def on_red_button_press(self, instance): #Kızgın
        red_sentences = [
            "Belki ben bir hata yapmışımdır, bilmiyorum. Bir hata yaptıysam özür dilerim, eğer ben yapmadıysam üzülme çünkü diğerleri umrumuzda olmamalı :)"
            "Kolay sinirlenirsin ama boş sinirlenmezsin, eminim ki sinirlenme sebebin çok sinir bozucudur ama sabretmeden de çözülmüyor :( Ben yanındayım."
            "Bağırmak içinde topladığın enerjiyi boşaltmak için en iyi yoldur, ama bazen bunu yapamazsın. İçini bir yerlere yazıp dökebilirsin veya belki bana yazarsın, okurum."
            "Her zaman yanındayım. Çözeriz, sakin ol"
            "Bazen sadece sabretmek gerekir güzelim hep bir şeyler yaparak çözemezsin. Sabrederiz ve çözeriz hep senin tarafındayım."
            "Senin yaşadığın şeyi bir tek sen yaşamamışsındır herkes yaşamıştır. Demek istediğim şey bunun üstesinden gelinebilmiş sen de gelebilirsin güzel yüzlüm canını sıkma."
        ]
        self.label.text = random.choice(red_sentences)

if __name__ == '__main__':
    MyApp().run()