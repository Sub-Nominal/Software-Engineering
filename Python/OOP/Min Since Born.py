from datetime import datetime, timedelta
import inflect
p = inflect.engine()
def main():
    bday = datetime.strptime(input("Enter Birthday: "), '%Y-%m-%d')
    dt= datetime.today()
    diff = dt - bday
    min = diff/timedelta(minutes=1)
    min = int(min)
    op = p.number_to_words(min)
    print(op.capitalize(), 'minutes')
main()