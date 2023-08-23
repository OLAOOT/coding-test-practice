from itertools import product

def solution(users, emoticons):
    answer = [-1, -1]
    discount_types = [10, 20, 30, 40]
    
    for discounts in product(discount_types, repeat=len(emoticons)):
        user_join, sale_amount = 0, 0
        
        for user in users:
            purchase_sum = 0
            discount_limit, price_limit = user
            
            for idx, discount in enumerate(discounts):
                if discount_limit <= discount:
                    purchase_sum += emoticons[idx] * (1 - discount * 0.01)
            
            if purchase_sum >= price_limit:
                user_join += 1
            else:
                sale_amount += purchase_sum
        if user_join > answer[0] or (user_join == answer[0] and sale_amount > answer[1]):
            answer = [user_join, sale_amount]
    
    return answer