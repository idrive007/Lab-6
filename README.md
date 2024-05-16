# Звіт з лабораторної роботи №6. Дублювання коду.
> Виконала студентка групи ІКМ-М223в **Павленко Дарина**
> 
### Мета: Рефакторінг коду з проблемою «Дублювання коду».

### Завдання 1: Наданий код
    
   
    def calculate_total_price(product_prices, discount):
        total_price = 0
        for price in product_prices:
            if discount:
                total_price += price * 0.9  # 10% discount
            else:
                total_price += price
        return total_price

    def calculate_total_price_with_tax(product_prices, discount, tax_rate):
        total_price = 0
        for price in product_prices:
            if discount:
                total_price += price * 0.9  # 10% discount
            else:
                total_price += price
        total_price *= (1 + tax_rate)
        return total_price



### Рішення

В оригінальному коді присутнє дублювання логіки, а саме, блок коду, який обчислює ціну товару з урахуванням знижки, повторюється в обох функціях calculate_total_price і calculate_total_price_with_tax. Це призводить до небажаного ефекту, коли зміни в логіці знижки потрібно вносити у двох місцях, що може призвести до помилок.

    def calculate_total_price(product_prices, discount):
        total_price = 0
        for price in product_prices:
            total_price += apply_discount(price, discount)
        return total_price

    def apply_discount(price, discount):
        if discount:
            return price * 0.9  
        else:
            return price

    def calculate_total_price_with_tax(product_prices, discount, tax_rate):
        total_price = calculate_total_price(product_prices, discount)
        total_price *= (1 + tax_rate)
        return total_price

Дублювання було усунено за допомогою використання відокремлення методу. Функція apply_discount створюється для обчислення ціни товару з урахуванням знижки, і вона використовується як в calculate_total_price, так і в calculate_total_price_with_tax. Це дозволяє знизити дублювання коду та полегшити його підтримку, оскільки зміни в логіці знижки потрібно вносити лише в одному місці - у функції apply_discount.


### Завдання 2: Наданий код


    class DataAnalyzer:
        def __init__(self, data):
            self.data = data
  
    def _calculate_total_and_count(self):
        total = sum(self.data)
        count = len(self.data)
        return total, count

    def calculate_total(self):
        total, _ = self._calculate_total_and_count()
        return total

    def calculate_average(self):
        total, count = self._calculate_total_and_count()
        return total / count if count != 0 else 0

    def calculate_minimum(self):
        return min(self.data) if self.data else None

    def calculate_maximum(self):
        return max(self.data) if self.data else None


### Рішення

В оригінальному коді бачимо дублювання логіки обчислення загальної суми та кількості елементів. Ця логіка повторюється в методах calculate_total та calculate_average. Можна відокремити цей блок коду в окремий метод, щоб уникнути дублювання.

    class DataAnalyzer:
        def __init__(self, data):
        self.data = data

    def _calculate_total_and_count(self):
        total = sum(self.data)
        count = len(self.data)
        return total, count

    def _calculate_total(self):
        total, _ = self._calculate_total_and_count()
        return total

    def _calculate_average(self):
        total, count = self._calculate_total_and_count()
        return total / count if count != 0 else 0

    def calculate_total(self):
        return self._calculate_total()

    def calculate_average(self):
        return self._calculate_average()

    def calculate_minimum(self):
        return min(self.data) if self.data else None

    def calculate_maximum(self):
        return max(self.data) if self.data else None
        
Методи calculate_total та calculate_average тепер використовують внутрішній метод _calculate_total_and_count для обчислення необхідних значень, уникнувши таким чином дублювання коду.
