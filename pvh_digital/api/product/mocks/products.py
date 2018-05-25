"""
Mock objects for Product Details API
"""

PRODUCTS = {
    "abcdefghijklmnop01": {
        "id": "abcdefghijklmnop01",
        "store_id": "abcdefgh_store_1",
        "size_guide": "URL(html,pdf,png)",
        "style_description": "SLIM FIT MONOGRAM LOGO T-SHIRT",
        "locale": "en-US",
        "price": {
            "currency": "USD",
            "currency_sign": "$",
            "value": 39.5
        },
        "variants": {
            "100_101": "abcdefghijklmnop01",
            "100_102": "abcdefghijklmnop02",
            "100_103": "abcdefghijklmnop03",
            "100_104": "abcdefghijklmnop04",
            "200_101": "abcdefghijklmnop05",
            "200_102": "abcdefghijklmnop06",
            "200_103": "abcdefghijklmnop07",
            "200_104": "abcdefghijklmnop08",
            "300_101": "abcdefghijklmnop09",
            "300_102": "abcdefghijklmnop10",
            "300_103": "abcdefghijklmnop11",
            "300_104": "abcdefghijklmnop12"
        },
        "size_code": 101,
        "sizes_available": {
            "101": "S",
            "102": "M",
            "103": "L",
            "104": "XL"
        },
        "color_code": 100,
        "colors_available": {
            "100": "red",
            "200": "black",
            "300": "green"
        },
        "details": "cut in a slim fit, this short sleeve t-shirt is made with soft cotton, a crewneck, a straight hem and a compact monogram logo on the chest",
        "images": [
            {
                "actual": "http://via.placeholder.com/400?text=Image+1",
                "thumb": "http://via.placeholder.com/400?text=Image+1"
            },
            {
                "actual": "http://via.placeholder.com/400?text=Image+2",
                "thumb": "http://via.placeholder.com/400?text=Image+2"
            },
            {
                "actual": "http://via.placeholder.com/400?text=Image+3",
                "thumb": "http://via.placeholder.com/400?text=Image+3"
            },
            {
                "actual": "http://via.placeholder.com/400?text=Image+4",
                "thumb": "http://via.placeholder.com/400?text=Image+4"
            }
        ],
        "division_code": 123,
        "division_name": "WOMEN'S ACCESSORIES",
        "department_code": 423,
        "department_name": "EYEWEAR",
        "class_code": 143,
        "class_name": "EYEWEAR",
        "style_code": 212,
        "availability": {
            "nearby_stores": [
                {
                    "colors": [
                        "green",
                        "blue",
                        "red"
                    ],
                    "sizes": [
                        "S",
                        "M",
                        "L"
                    ],
                    "id": 999,
                    "name": "ABC Store 1"
                },
                {
                    "id": 998,
                    "name": "ABC Store 2"
                },
                {
                    "id": 997,
                    "name": "ABC Store 3"
                }
            ],
            "store": {
                "items_available": 5
            }
        }
    }
}
