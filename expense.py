class Expense:
    
    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        
        
    def __repr__(self):
        return f"Expense(name={self.name!r}, category={self.category!r}, amount={self.amount})" #we do not want it to store as a disk space we want it to store as a output variable