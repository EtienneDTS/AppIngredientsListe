from pathlib import Path
import json
import smtplib

CUR_DIR = Path(__file__).resolve().parent
DB = CUR_DIR/"data"/"db.json"

with open(DB, "r") as f:
    db_data = json.load(f)

class Cook:
    def get_recipe(self) -> list:
        recipe_list = []
        for recipe in db_data.keys() :
            recipe_list.append(recipe)
        return recipe_list

    def get_ingredients(self, recip) ->list:
        ingredients_list = []
        for ingredient in db_data.get(recip):
            ingredients_list.append(ingredient)
        return ingredients_list

    def send_mail(self,recipe, ingredient):
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        SMTP_USERNAME = "python.mail.for.app.hellofresh@gmail.com"
        SMTP_PASSWORD = "fswykjyavtsrplwe"
        EMAIL_FROM = "python.mail.for.app.hellofresh@gmail.com"
        EMAIL_TO = "eva.gherardi1@gmail.com"
        EMAIL_SUBJECT = "Attention:Bibi d'amour"
        EMAIL_MESSAGE = f'''Vous avez choisi ces recettes : {recipe},

Pour cela vous avez besoin de : {ingredient} '''
        s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        s.starttls()
        s.login(SMTP_USERNAME, SMTP_PASSWORD)
        message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE).encode('utf-8')
        s.sendmail(EMAIL_FROM, EMAIL_TO, message)
        s.quit()


if __name__ == "__main__":
    c = Cook()



