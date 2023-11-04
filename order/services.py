
from order.models import Summary


prices = {
    '華達士': ['1.5V,4V', 155, 400], 
    '弘揚': ['V,苔,A,芝', 400, 400, 375, 375], 
    '三乃': ['1.5V,大排,2A,2A苔', 155, 165, 160, 170], 
    '超品': ['V,2A,排,豆,起(12)', 400, 165, 175, 85, 255], 
    '新城': ['V', 450], 
    '美琳': ['排,牛排', 175, 225], 
    '洲河': ['V', 420], 
    '山河': ['V', 420], 
    '龍河': ['V', 420], 
    '神河': ['V', 420], 
    '鼎香': ['V', 450], 
    '橋山': ['V,排,培,哈', 440, 90, 235, 240], 
    '楊溢': ['V,排,培,哈', 440, 90, 235, 240], 
    '和達人五': ['V,小排,培,哈,起', 420, 90, 235, 240, 260], 
    '汀州路五': ['V,小排,培,哈,起', 420, 90, 235, 240, 260], 
    '瑞安街五': ['V,小排,培,起', 420, 90, 235, 260], 
    '和達人二': ['V,小排,培,哈,起', 420, 90, 255, 240, 260], 
    '汀州路二': ['V,小排,培,哈,起', 420, 90, 255, 240, 260], 
    '瑞安街二': ['V,小排,培,起', 420, 90, 255, 260], 
    '來可': ['V', 450], '桃鶯': ['V(箱),豆', 2700, 90], 
    '春日': ['V(箱),豆', 2700, 90], 
    '大興': ['V(箱),豆', 2700, 90], 
    '筱芸南平': ['V', 450], 
    '北大昇輝': ['V,豆', 450, 90], 
    '昇輝寶慶': ['V,豆', 450, 90], 
    '桃園寶慶': ['V,豆', 480, 90], 
    '百成一店': ['V(箱),豆', 2700, 90], 
    '北聖': ['V,豆', 450, 90],
    '筱芸中正': ['V', 450], 
    '大園果林': ['V(箱),豆', 2700, 90], 
    '云盛': ['V,排,培,哈', 450, 90, 245, 240], 
    '北大文化二路': ['V,豆', 450, 90], 
    '林口仁愛': ['V,豆', 450, 90], 
    '北大文化三路': ['V,豆', 450, 90], 
    '龍鳳': ['5V,排,4V', 500, 175, 400], 
    '深溪': ['V,豆', 450, 90], 
    '仁樂': ['V,豆', 450, 90], 
    '珍好味': ['V,豆', 450, 90], 
    '新豐': ['V,豆', 450, 90], 
    '福德': ['V,豆', 450, 90], 
    '筱芸中壢': ['V', 450]
}

def bill_overview(orders):
    total_sum = 0
    summaries = []
    for order in orders:
        items = order.item.split(',')
        num_items = order.num_item.split('.')
        company_price = prices[order.customer][1:]
        cur_sum = 0
        for price, item, num in zip(company_price, items, num_items):
            price_x_num = price * int(num)
            cur_row.append(Summary(id=order.id ,customer=order.customer, item=item, num=num, price=price, cur_sum=price_x_num))
            cur_sum += price * int(num)
        cur_row.append(Summary(id="total" ,customer=order.customer, item="-", num="-", price="-", cur_sum=cur_sum))
        total_sum += cur_sum
        summaries.append(cur_row)
        print(f'items = {items}')
        print(f'price = {company_price}')
        print(f'num_items = {num_items}')
        print(f'cur sum = {cur_sum}')

    summaries[len(orders) - 1].append(Summary(id=" " ,customer=" ", item=" ", num=" ", price=" ", cur_sum=" "))
    summaries[len(orders) - 1].append(Summary(id="總和" ,customer="-", item="-", num="-", price="-", cur_sum=total_sum))
    return summaries

def order_precess(unplitted):
    unplitted = unplitted.strip().split(',')
    return unplitted