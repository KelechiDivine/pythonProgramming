class Invoice():
    def __init__(self, a_part_number, a_part_description,
                 quantity_of_item_purchased, price_per_item):
        
        self.__part_number = a_part_number
        self.__part_description = a_part_description
        self.__item_purchased = quantity_of_item_purchased
        self.__price_item = price_per_item
    
    def __init__(self):
        pass
    
    
    def set_part_number(self, varPartNumber) -> str:
        self.__part_number = varPartNumber
        
    def set_part_description(self, varPartDescription) -> str:
        self.__part_description = varPartDescription
        
    def set_item_purchased(self, varItemPurchased)->int:
        self.__item_purchased = varItemPurchased
        
    def set_price_item(self, varPriceItem)-> float:
        self.__price_item = varPriceItem
    
        if varPriceItem < 0 :
            self.set_price_item(0.0)
            print("Value has been set to 0.0")
        if varPriceItem > 0:
            print("Hiii")
        
    def get_part_number(self):
        return self.__part_number
    
    def get_description(self):
        return self.__part_description
    
    def get_item_purchased(self):
        return self.__item_purchased
    
    def get_price_item(self):
        return self.__price_item

    
    value = get_price_item() * get_item_purchased()
   
    def get_invoice_amount(self):
        val =
        
        def result(self):
            result_var = value
            
        result()
    get_invoice_amount()
    