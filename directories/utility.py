class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

class Search():

    def __init__(self, form):
        if form.is_valid():
            matches = Stack()

            # SWITCH CASE alternative, input category and return list of field names for associated subcategories
            sub_categories = sub_category_switcher(form['yp_category'])
            query = form['search_terms']
            search_terms = False if query == '' else query

            if search_terms == True:
                required_search = Dentist.objects.filter(
                    (Q(location__icontains=location) &
                    Q(yp_category__icontains=category)) &
                    (Q(name__icontains=search_terms) |
                    Q(city__icontains=search_terms) |
                    Q(yp_extra_info__icontains=search_terms) |
                    Q(yp_category__icontains=search_terms) |
                    Q(search_tree__icontains=search_terms))
                )
            else:
                required_search = Dentist.objects.filter(
                    Q(location__icontains=location) &
                    Q(yp_category__icontains=category)
                )
            for result in required_search:
                for key in keys():
                    if literal_eval(result.search_tree)[key] == self.form[key]:
                        matches.push(result)
            self.matches = matches
        else:
            self.form = None
    

            
            
    # Takes clean form as input,
    # returns list of matches as SQLAlchemy records

    # takes search category as argument, returns list of form field keys associated with given category
    def sub_category_switcher(self, category):
        switcher = {
            'Contractor' : ['contractor_category'],
            'Dentist' : ['insurance'],
            'Lawyer' : ['None'],
            'Restaurant' : ['None'],
            
        }
        return switcher.get(category)

        
    

            

        # for result in required_search:
        #     search_tree = literal_eval(result.search_tree)
        #     score = 0
        #     next_match = ()
        #     current_match = ()
            
        #     for key in search_tree.keys():
        #         if clean_form[key] == search_tree[key]:
        #             score += 1

        #     result_score = (result, score)
        #     if matches.is_empty():
        #         print("empty")
        #         print(matches)
        #         matches.push(result_score)
        #         next_match = result_score
        #     else:

        #         current_match = result_score
        #         while current_match[1] < next_match[1]:
        #             overflow.push(matches.pop())
        #         matches.push(current_match)
        #         for x in range(0, len(overflow) - 1):
        #             if x == len(overflow) - 1:
        #                 next_match = overflow.pop()
        #                 matches.push(next_match)
        #             else:
        #                 matches.push(overflow.pop())
                    

        # return matches