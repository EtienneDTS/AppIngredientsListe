from PySide2 import QtWidgets, QtGui
import api


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = api.Cook()
        self.setWindowTitle("Recette HelloFresh")
        self.left = 900
        self.top = 300
        self.width = 500
        self.height = 700
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setup_ui()
        self.set_cbb()
        self.set_connection()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.cbb_choice_recipe = QtWidgets.QComboBox()
        self.label1 = QtWidgets.QLabel("Les recettes que j'ai choisi.")
        self.lst_listRecipe = QtWidgets.QListWidget()
        self.btn_removeRecipe = QtWidgets.QPushButton("Retirer la recette.")
        self.label2 = QtWidgets.QLabel("Ma liste de course.")
        self.lst_listIngredients = QtWidgets.QListWidget()
        self.btn_sendMail = QtWidgets.QPushButton("Envoyé la liste de course par email")

        self.main_layout.addWidget(self.cbb_choice_recipe)
        self.main_layout.addWidget(self.label1)
        self.main_layout.addWidget(self.lst_listRecipe)
        self.main_layout.addWidget(self.btn_removeRecipe)
        self.main_layout.addWidget(self.label2)
        self.main_layout.addWidget(self.lst_listIngredients)
        self.main_layout.addWidget(self.btn_sendMail)

    def set_cbb(self):
        recipe = self.c.get_recipe()
        for i in recipe:
            self.cbb_choice_recipe.addItem(i)

    def set_connection(self):
        self.cbb_choice_recipe.activated.connect(self.select_recipe)
        self.btn_removeRecipe.clicked.connect(self.remove_recipe)
        self.btn_sendMail.clicked.connect(self.send_mail)

    def select_recipe(self):
        recipe = self.cbb_choice_recipe.currentText()
        self.lst_listRecipe.addItem(recipe)
        ingredients = self.c.get_ingredients(recipe)
        for ingredient in ingredients:
            self.lst_listIngredients.addItem(ingredient)

    def remove_recipe(self):
        for selected_item in self.lst_listRecipe.selectedItems() :
            self.lst_listRecipe.takeItem(self.lst_listRecipe.row(selected_item))
        self.lst_listIngredients.clear()
        items = []
        for x in range(self.lst_listRecipe.count()):
            items.append(self.lst_listRecipe.item(x).text())
        for item in items:
            ingredients = self.c.get_ingredients(item)
            for ingredient in ingredients :
                self.lst_listIngredients.addItem(ingredient)

    def send_mail(self):
        recipe = []
        ingredient = []
        for x in range(self.lst_listRecipe.count()):
            recipe.append(self.lst_listRecipe.item(x).text())
        for x in range(self.lst_listIngredients.count()):
            ingredient.append(self.lst_listIngredients.item(x).text())
        self.c.send_mail(recipe,ingredient)
        self.lst_listRecipe.clear()
        self.lst_listIngredients.clear()
        self.lst_listRecipe.addItem('''Vous avez reçu un email :
Il comprend les recettes que vous avez choisi,
ainsi que les ingrédients necessaires pour les préparer.
          
Bonne journée.''')



if __name__ == "__main__" :
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    app.exec_()

