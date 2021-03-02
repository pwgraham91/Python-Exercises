raw = ['Artisan', 'live-edge', 'ugh', 'DIY', 'poutine', 'flexitarian', 'leggings', 'lo-fi', '3', 'wolf', 'moon',
           'biodiesel', 'ennui', 'kombucha', 'gentrify', 'XOXO', 'health', 'goth.', 'Brunch', 'fixie', 'put', 'a',
           'bird', 'on', 'it', 'you', 'probably', "haven't", 'heard', 'of', 'them', 'photo', 'booth', 'hell', 'of',
           'bespoke', 'bicycle', 'rights.', 'Mustache', 'neutra', 'truffaut,', 'DIY', 'hoodie', 'slow-carb', 'pop-up',
           'man', 'braid', 'pitchfork.', 'Artisan', 'activated', 'charcoal', 'tofu', 'shoreditch,', 'pug', 'readymade',
           'church-key', '+1', 'iPhone', 'normcore', 'fingerstache', 'keytar', 'truffaut', 'lumbersexual', 'paleo.',
           'Crucifix', 'austin', 'cred', 'taxidermy', 'truffaut', 'bicycle', 'rights', 'hell', 'of', 'pabst',
           'activated', 'charcoal.', 'Narwhal', 'forage', 'letterpress', 'paleo', 'gentrify', 'la', 'croix', 'synth',
           'freegan', 'bespoke', 'keytar.', 'Dreamcatcher', 'bespoke', 'bushwick', 'listicle', 'lomo.']

added_content = ['Kombucha', 'pop-up', 'blog', 'bitters', 'quinoa', 'blue', 'bottle', 'intelligentsia', 'flexitarian',
                 'copper', 'mug', 'pour-over', 'messenger', 'bag', "90's", 'neutra', 'lomo.', 'Hella', "90's",
                 'everyday', 'carry', 'mlkshk', 'scenester', 'four', 'dollar', 'toast', 'live-edge', 'cliche', 'wolf',
                 'truffaut', 'cronut', 'ramps', 'succulents.', 'Slow-carb', 'fam', 'blue', 'bottle', 'adaptogen',
                 'hammock', 'shoreditch.', 'Pour-over', 'fingerstache', 'mlkshk', 'tofu', 'normcore.', 'Tote', 'bag',
                 'four', 'dollar', 'toast', 'lumbersexual', 'raw', 'denim', 'venmo', 'kickstarter', 'fixie',
                 'stumptown', 'letterpress', 'locavore', 'echo', 'park', 'unicorn.', 'Forage', 'cardigan', 'tote',
                 'bag', 'mlkshk.', 'Unicorn', 'la', 'croix', 'kickstarter', 'coloring', 'book', 'ugh', 'tilde',
                 'sourdough', 'starter.']


""" 
Part 1: We have a list of content and we want to inject ads after the 3rd piece of content and then after every 4 
pieces.

Part 2: We have 20 more pieces of content to add to the list and there should be ads between every 4 of them as a 
continuation of the previous list.
"""
def evenly_ad_ads(content_with_ads, content_without_ads, start_ad_index, ad_interval):
    # add one to make it so ads go after the interval instead of on the interval
    ad_interval = ad_interval + 1

    content_length = len(content_without_ads)
    content_counter = 0

    # iterate through the list and add either an AD or content until there is no more content to add
    while content_counter < content_length:
        content_with_ads_size = len(content_with_ads)
        if content_with_ads_size == start_ad_index or (content_with_ads_size - start_ad_index) % ad_interval == 0:
            content_with_ads.append("AD!")
        else:
            content_with_ads.append(content_without_ads[content_counter])
            content_counter += 1

    return content_with_ads

"""
what if we need to insert content into the middle of the list
"""
def insert_content(content_with_ads, inserted_content, insert_index, start_ad_index, ad_interval):
    # divide the list at the spot of insertion. Everything before the insertion spot should stay the same.
    content_with_ads_left = content_with_ads[:insert_index]
    content_with_ads_right = content_with_ads[insert_index:]
    # remove all of the ads after the insertion and re-add the ads after insertion
    content_without_ads_right = list(filter(lambda x: x != 'AD!', content_with_ads_right))
    inserted_content.extend(content_without_ads_right)

    return evenly_ad_ads(content_with_ads_left, inserted_content, start_ad_index, ad_interval)



parts_1_2 = evenly_ad_ads(evenly_ad_ads([], raw, 3, 4), added_content, 3, 4)
inserted_list = insert_content(parts_1_2, ["INSERT1", "INSERT2", "INSERT3", "INSERT4"], 1, 3, 4)
