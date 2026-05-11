#=============================================================================
#                           Recommendation model draft
# Match case for skin type and sesnsitivity level, 
# checks the ingredients for products and determines if they're safe for user
#=============================================================================


def recommend_products(user, products):         
    recommendations = []
    for product in products:

        safe = True
        for ingredient in product.ingredients:

            match user.skin_type:
                case "acne_prone":
                    if ingredient.comedogenic_grade >= 3:
                        safe = False
                        break
                case "sensitive":
                    if ingredient.irritation_grade >= 3:
                        safe = False
                        break
                case "dry":
                    pass
                case "oily":
                    pass
            
            match user.sens_level:
                case "low":
                    if ingredient.irritation_grade >= 1:
                        safe = True
                        print ("low irritation grade, use with caution")
                case "medium":
                    if ingredient.irritation_grade >= 2:
                        safe = False
                        break
                case "high":
                    if ingredient.irritation_grade >= 3:
                        safe = False
                        break