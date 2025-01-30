import json
from typing import List, Dict
from .mill import Mills
from .bean import Beans
from .prepartion import Preparations
from .brew import Brews


class BeanConquerorParser:
    def __init__(self, json_file: str):
        with open(json_file) as f:
            self.data = json.load(f)

    @property
    def mills(self) -> Mills:
        """
        Examples:
        [
            {
                "name": "Sage Barista Touch",
                "note": "",
                "config": {
                  "uuid": "8bd4c8dd-0ef6-449c-81cf-36cd90e84738",
                  "unix_timestamp": 1701453420
                },
                "finished": false,
                "attachments": [
                  "/beanconqueror_image32.jpg"
                ]
            },
        ]

        Returns:
            List[Dict]: List of mill data

        """
        return Mills(self.data.get("MILL"))

    @property
    def beans(self) -> Beans:
        """
        Examples:
            {
                "name": "Mente Bello",
                "buyDate": "2023-11-28T11:59:00.000Z",
                "roastingDate": "2023-12-17T17:51:00.000Z",
                "note": "一包250g，用app的时候只剩下30g左右了，线下购买，一包下来，还没找到适合颗粒度",
                "roaster": "Thomson",
                "config": {
                    "uuid": "6ba75c16-47fa-4361-bbe7-ebc10e6ed0d6",
                    "unix_timestamp": 1701453304
                },
                "roast": "CITY_ROAST",
                "roast_range": 0,
                "roast_custom": "",
                "beanMix": "BLEND",
                "aromatics": "Red Fruit，chocolate，agave",
                "weight": 20,
                "finished": true,
                "cost": 9.9,
                "attachments": [],
                "decaffeinated": false,
                "cupping_points": "",
                "bean_roasting_type": "ESPRESSO",
                "bean_information": [
                    {
                        "country": "Colombia",
                        "processing": "washed",
                        "variety": "Caturra"
                    }
                ],
                "url": "",
                "ean_article_number": "",
                "bean_roast_information": {
                    "drop_temperature": 0,
                    "roast_length": 0,
                    "roaster_machine": "",
                    "green_bean_weight": 0,
                    "outside_temperature": 0,
                    "humidity": 0,
                    "bean_uuid": "",
                    "first_crack_minute": 0,
                    "first_crack_temperature": 0,
                    "second_crack_minute": 0,
                    "second_crack_temperature": 0
                },
                "rating": 1,
                "qr_code": "",
                "favourite": false,
                "shared": false,
                "cupping": {
                    "body": 0,
                    "brightness": 0,
                    "clean_cup": 0,
                    "complexity": 0,
                    "cuppers_correction": 0,
                    "dry_fragrance": 0,
                    "finish": 0,
                    "flavor": 0,
                    "sweetness": 0,
                    "uniformity": 0,
                    "wet_aroma": 0,
                    "notes": ""
                },
                "cupped_flavor": {
                    "predefined_flavors": {},
                    "custom_flavors": []
                }
            }

        Returns:
            List[Dict]: List of bean data
        """
        return Beans(self.data.get("BEANS"))

    @property
    def brews(self) -> Brews:
        """
        Examples:
            {
                "grind_size": 17,
                "grind_weight": 17,
                "method_of_preparation": "f19f7868-fa04-4b49-b96e-eeaa66696209",
                "mill": "8bd4c8dd-0ef6-449c-81cf-36cd90e84738",
                "mill_speed": 0,
                "mill_timer": 0,
                "pressure_profile": "",
                "bean": "6ba75c16-47fa-4361-bbe7-ebc10e6ed0d6",
                "brew_temperature_time": 0,
                "brew_temperature": 0,
                "brew_time": 24,
                "brew_quantity": 0,
                "brew_quantity_type": "GR",
                "note": "有苦涩味",
                "rating": 2,
                "coffee_type": "",
                "coffee_concentration": "",
                "coffee_first_drip_time": 0,
                "coffee_blooming_time": 0,
                "attachments": [],
                "config": {
                    "uuid": "fe329f49-0f23-459d-96d8-8cbb3b8f4b7f",
                    "unix_timestamp": 1701513621
                },
                "tds": 0,
                "brew_beverage_quantity": 34,
                "brew_beverage_quantity_type": "GR",
                "brew_time_milliseconds": 0,
                "brew_temperature_time_milliseconds": 0,
                "coffee_first_drip_time_milliseconds": 0,
                "coffee_blooming_time_milliseconds": 0,
                "coordinates": {
                    "accuracy": null,
                    "altitude": null,
                    "altitudeAccuracy": null,
                    "heading": null,
                    "latitude": null,
                    "longitude": null,
                    "speed": null
                },
                "cupping": {
                    "body": 0,
                    "brightness": 0,
                    "clean_cup": 0,
                    "complexity": 0,
                    "cuppers_correction": 0,
                    "dry_fragrance": 0,
                    "finish": 0,
                    "flavor": 0,
                    "sweetness": 0,
                    "uniformity": 0,
                    "wet_aroma": 0,
                    "notes": ""
                },
                "cupped_flavor": {
                    "predefined_flavors": {},
                    "custom_flavors": []
                },
                "method_of_preparation_tools": [],
                "bean_weight_in": 0,
                "favourite": false,
                "best_brew": false,
                "water": "",
                "vessel_name": "",
                "vessel_weight": 0,
                "flow_profile": "",
                "preparationDeviceBrew": {
                    "type": "NONE"
                }
            }

        Returns:
            List[Dict]: List of brew data

        """
        return Brews(self.data.get("BREWS"))

    @property
    def preparations(self) -> Preparations:
        """
        Examples:
            {
                "name": "Sage Barista Express",
                "note": "",
                "config": {
                    "uuid": "f19f7868-fa04-4b49-b96e-eeaa66696209",
                    "unix_timestamp": 1701453723
                },
                "type": "PORTAFILTER",
                "style_type": "ESPRESSO",
                "finished": false,
                "use_custom_parameters": true,
                "manage_parameters": {
                    "bean_type": true,
                    "brew_temperature_time": false,
                    "brew_time": true,
                    "grind_size": true,
                    "grind_weight": true,
                    "mill": true,
                    "mill_timer": false,
                    "method_of_preparation": true,
                    "brew_quantity": false,
                    "brew_temperature": false,
                    "note": true,
                    "coffee_type": false,
                    "coffee_concentration": false,
                    "coffee_first_drip_time": true,
                    "coffee_blooming_time": true,
                    "rating": true,
                    "mill_speed": false,
                    "pressure_profile": false,
                    "tds": false,
                    "brew_beverage_quantity": true,
                    "attachments": false,
                    "set_last_coffee_brew": false,
                    "set_custom_brew_time": true,
                    "method_of_preparation_tool": true,
                    "water": false,
                    "bean_weight_in": false,
                    "vessel": false
                },
                "default_last_coffee_parameters": {
                    "bean_type": true,
                    "brew_temperature_time": false,
                    "brew_time": true,
                    "grind_size": true,
                    "grind_weight": true,
                    "mill": true,
                    "mill_timer": false,
                    "method_of_preparation": true,
                    "brew_quantity": false,
                    "brew_temperature": true,
                    "note": false,
                    "coffee_type": true,
                    "coffee_concentration": true,
                    "coffee_first_drip_time": true,
                    "coffee_blooming_time": true,
                    "rating": false,
                    "mill_speed": false,
                    "pressure_profile": false,
                    "tds": false,
                    "brew_beverage_quantity": true,
                    "method_of_preparation_tool": false,
                    "water": false,
                    "bean_weight_in": false,
                    "vessel": false
                },
                "visible_list_view_parameters": {
                    "bean_type": true,
                    "brew_temperature_time": false,
                    "brew_time": true,
                    "grind_size": true,
                    "grind_weight": true,
                    "mill": true,
                    "method_of_preparation": true,
                    "brew_quantity": true,
                    "mill_speed": true,
                    "mill_timer": false,
                    "brew_beverage_quantity": true,
                    "tds": true,
                    "coffee_first_drip_time": true,
                    "pressure_profile": true,
                    "brew_temperature": true,
                    "note": false,
                    "coffee_type": false,
                    "coffee_concentration": false,
                    "coffee_blooming_time": false,
                    "rating": true,
                    "method_of_preparation_tool": false,
                    "water": false,
                    "bean_weight_in": false,
                    "vessel": false
                },
                "repeat_coffee_parameters": {
                    "bean_type": true,
                    "brew_temperature_time": true,
                    "brew_time": true,
                    "grind_size": true,
                    "grind_weight": true,
                    "mill": true,
                    "mill_timer": true,
                    "method_of_preparation": true,
                    "brew_quantity": false,
                    "brew_temperature": true,
                    "note": true,
                    "coffee_type": true,
                    "coffee_concentration": true,
                    "coffee_first_drip_time": false,
                    "coffee_blooming_time": true,
                    "rating": true,
                    "mill_speed": true,
                    "pressure_profile": true,
                    "tds": true,
                    "brew_beverage_quantity": false,
                    "method_of_preparation_tool": true,
                    "water": true,
                    "bean_weight_in": true,
                    "vessel": true,
                    "repeat_coffee_active": false
                },
                "brew_order": {
                    "before": {
                        "bean_type": 1,
                        "bean_weight_in": 2,
                        "grind_weight": 3,
                        "mill": 4,
                        "grind_size": 5,
                        "mill_timer": 6,
                        "mill_speed": 7,
                        "method_of_preparation": 8,
                        "method_of_preparation_tool": 9,
                        "brew_temperature": 10,
                        "water": 11,
                        "vessel": 12,
                        "pressure_profile": 13
                    },
                    "while": {
                        "brew_temperature_time": 1,
                        "brew_time": 2,
                        "coffee_blooming_time": 3,
                        "coffee_first_drip_time": 4
                    },
                    "after": {
                        "coffee_type": 1,
                        "coffee_concentration": 2,
                        "brew_quantity": 3,
                        "brew_beverage_quantity": 4,
                        "tds": 5,
                        "rating": 6,
                        "note": 7,
                        "set_custom_brew_time": 8,
                        "attachments": 9
                    }
                },
                "tools": [
                    {
                        "name": "53mm protafilter",
                        "config": {
                            "uuid": "ad232722-5227-4d49-8bc8-156e751f2e25",
                            "unix_timestamp": 1702318528
                        },
                        "archived": false
                    },
                    {
                        "name": "53mm bottomless protafilter",
                        "config": {
                            "uuid": "0f2c2a6c-35f2-4ba3-a353-5603d55658de",
                            "unix_timestamp": 1722074265
                        },
                        "archived": false
                    },
                    {
                        "name": "51mm bottomless protafilter",
                        "config": {
                            "uuid": "3024a0ed-d316-419f-a763-3ea6526f2e8d",
                            "unix_timestamp": 1727444426
                        },
                        "archived": false
                    },
                    {
                        "name": "53mm MHW-3Bomber puck screen",
                        "config": {
                            "uuid": "886464ee-1388-4722-8ce8-a64a7a22f30a",
                            "unix_timestamp": 1734779182
                        },
                        "archived": false
                    },
                    {
                        "name": " 53mm Bincoo puck screen",
                        "config": {
                            "uuid": "3a2df60b-59a9-4f4a-a072-23228497a83c",
                            "unix_timestamp": 1734779251
                        },
                        "archived": false
                    },
                    {
                        "name": "53mm Gritty puck screen",
                        "config": {
                            "uuid": "0f006355-6c06-47a1-8013-b23f6b8e8ab8",
                            "unix_timestamp": 1734779310
                        },
                        "archived": false
                    }
                ],
                "attachments": [
                    "/beanconqueror_image5.jpg"
                ],
                "connectedPreparationDevice": {
                    "type": "NONE",
                    "url": "",
                    "customParams": {}
                }
            }

        Returns:
            List[Dict]: List of preparation data

        """
        return Preparations(self.data.get("PREPARATION"))
