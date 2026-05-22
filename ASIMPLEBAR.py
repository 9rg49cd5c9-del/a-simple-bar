#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ============================================
# A SIMPLE BAR - CAMPING EDITION
# ============================================

import streamlit as st
import pandas as pd
import base64
from pathlib import Path


st.set_page_config(
    page_title="A Simple Bar",
    page_icon="🍹",
    layout="wide"
)


# ============================================
# IMAGE HELPERS
# ============================================

def get_base64_image(image_path):
    image_path = Path(image_path)

    if not image_path.exists():
        return ""

    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# Header image path
bg_image = get_base64_image("camping.jpg")

if bg_image:
    hero_background = f"""
    background-image:
        linear-gradient(rgba(0,0,0,0.18), rgba(0,0,0,0.18)),
        url("data:image/jpg;base64,{bg_image}");
    """
else:
    hero_background = """
    background: linear-gradient(135deg, #18392B 0%, #10251C 100%);
    """


# ============================================
# DRINK DATA
# ============================================

drinks = [
    {
    "name": "Fig Bee’s Knees",
    "category": "Cocktails",
    "description": "Gin, fig jam, lemon, and honey thyme syrup with a smooth botanical finish.",
    "emoji": "🍯",
    "strength": "Medium",
    "vibe": "Elegant",
    "tags": ["Gin", "Fig", "Honey", "Citrus"],
    "flavor": "Fruity",
    "ingredients": [
        "1 tbsp fig jam",
        "2 oz gin",
        "3/4 oz lemon juice",
        "3/4 oz honey thyme simple syrup",
        "Ice",
        "Thyme leaves for garnish",
        "Fresh fig slices for garnish",
    ],
    "recipe": [
        "Chill a coupe glass before starting.",
        "Add fig jam, gin, lemon juice, and honey thyme syrup to a shaker.",
        "Shake without ice first until the fig jam fully breaks down.",
        "Add ice and shake again for 10–15 seconds until well chilled.",
        "Fine strain into the chilled coupe glass.",
        "Garnish with thyme leaves and fresh fig slices.",
    ],
},
{
    "name": "Nuts & Berries",
    "category": "Cocktails",
    "description": "A creamy dessert cocktail with Frangelico, Chambord, and cream.",
    "emoji": "🥜",
    "strength": "Medium",
    "vibe": "Dessert",
    "tags": ["Frangelico", "Chambord", "Creamy", "Sweet"],
    "flavor": "Dessert",
    "ingredients": [
        "1 oz Frangelico",
        "1 oz Chambord",
        "2 oz cream or half-and-half",
        "Ice",
        "Optional raspberry garnish",
    ],
    "recipe": [
        "Fill a cocktail shaker with ice.",
        "Add Frangelico, Chambord, and cream.",
        "Shake well until chilled and smooth.",
        "Strain into a rocks glass over fresh ice.",
        "Optional: garnish with raspberries or a dusting of cocoa powder.",
    ],
},
{
    "name": "Peach Bellini",
    "category": "Cocktails",
    "description": "A light sparkling cocktail with peach purée and chilled prosecco.",
    "emoji": "🍑",
    "strength": "Light",
    "vibe": "Brunch",
    "tags": ["Peach", "Prosecco", "Sparkling", "Refreshing"],
    "flavor": "Fruity",
    "image": "images/peach_bellini.jpg",
    "ingredients": [
        "2 oz peach purée",
        "4 oz chilled prosecco",
        "Optional peach slice for garnish",
    ],
    "recipe": [
        "Add peach purée to a champagne flute.",
        "Slowly pour chilled prosecco over the purée.",
        "Stir gently to combine.",
        "Optional: garnish with a peach slice.",
        "Serve immediately while cold and bubbly.",
    ],
},
{
    "name": "Pistachio Martini",
    "category": "Cocktails",
    "description": "A creamy dessert martini with pistachio cream, vanilla vodka, and nutty sweetness.",
    "emoji": "💚",
    "strength": "Medium",
    "vibe": "Dessert",
    "tags": ["Pistachio", "Creamy", "Sweet", "Dessert"],
    "flavor": "Dessert",
    "image": "images/pistachio_martini.jpg",
    "ingredients": [
        "2 oz vanilla vodka",
        "1 oz pistachio cream liqueur",
        "1 oz Irish cream liqueur",
        "1 oz heavy cream or half-and-half",
        "Ice",
        "Crushed pistachios for rim (optional)",
    ],
    "recipe": [
        "Optional: rim a martini glass with crushed pistachios.",
        "Fill a shaker with ice.",
        "Add vanilla vodka, pistachio liqueur, Irish cream, and cream.",
        "Shake vigorously until cold and creamy.",
        "Strain into a chilled martini glass.",
        "Optional: garnish with crushed pistachios.",
    ],
},
{
    "name": "Lemon Drop Martini",
    "category": "Cocktails",
    "description": "A bright citrus martini with vodka, fresh lemon juice, and a sugared rim.",
    "emoji": "🍋",
    "strength": "Strong",
    "vibe": "Refreshing",
    "tags": ["Vodka", "Lemon", "Citrus", "Classic"],
    "flavor": "Lemon / Citrus",
    "image": "images/lemon_drop_martini.jpg",
    "ingredients": [
        "2 oz vodka",
        "1 oz triple sec or orange liqueur",
        "1 oz fresh lemon juice",
        "1/2 oz simple syrup",
        "Ice",
        "Sugar for rim",
        "Lemon twist or slice for garnish",
    ],
    "recipe": [
        "Rim a martini glass with sugar using a lemon wedge.",
        "Fill a cocktail shaker with ice.",
        "Add vodka, triple sec, lemon juice, and simple syrup.",
        "Shake vigorously until very cold.",
        "Strain into the prepared martini glass.",
        "Garnish with a lemon twist or slice.",
    ],
},
{
    "name": "Sex on the Island",
    "category": "Cocktails",
    "description": "A tropical vodka cocktail with peach, cranberry, and pineapple flavors.",
    "emoji": "🏝️",
    "strength": "Medium",
    "vibe": "Tropical",
    "tags": ["Vodka", "Peach", "Pineapple", "Tropical"],
    "flavor": "Fruity",
    "image": "images/sex_on_the_island.jpg",
    "ingredients": [
        "1 oz vodka",
        "1 oz peach schnapps",
        "2 oz pineapple juice",
        "2 oz cranberry juice",
        "Ice",
        "Orange slice or cherry for garnish",
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add vodka, peach schnapps, pineapple juice, and cranberry juice.",
        "Shake until chilled.",
        "Strain into a glass filled with fresh ice.",
        "Garnish with an orange slice or cherry.",
    ],
},
{
    "name": "Pink Flamingo",
    "category": "Cocktails",
    "description": "A bright tropical cocktail with coconut rum, pineapple, and pink lemonade.",
    "emoji": "🦩",
    "strength": "Light",
    "vibe": "Beachy",
    "tags": ["Coconut", "Pineapple", "Tropical", "Sweet"],
    "flavor": "Fruity",
    "image": "images/pink_flamingo.jpg",
    "ingredients": [
        "2 oz coconut rum",
        "2 oz pineapple juice",
        "2 oz pink lemonade",
        "Splash of lemon-lime soda",
        "Ice",
        "Cherry or pineapple wedge for garnish",
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add coconut rum, pineapple juice, and pink lemonade.",
        "Shake until chilled.",
        "Pour into a glass filled with fresh ice.",
        "Top with a splash of lemon-lime soda.",
        "Garnish with a cherry or pineapple wedge.",
    ],
},
{
    "name": "June Bug",
    "category": "Cocktails",
    "description": "A tropical melon cocktail with coconut, banana, pineapple, and citrus flavors.",
    "emoji": "🪲",
    "strength": "Medium",
    "vibe": "Tropical",
    "tags": ["Melon", "Banana", "Coconut", "Pineapple"],
    "flavor": "Fruity",
    "image": "images/june_bug.jpg",
    "ingredients": [
        "1 oz Midori melon liqueur",
        "1 oz coconut rum",
        "1 oz banana liqueur",
        "2 oz pineapple juice",
        "1 oz sweet and sour mix",
        "Ice",
        "Pineapple wedge or cherry for garnish",
    ],
    "recipe": [
        "Fill a cocktail shaker with ice.",
        "Add Midori, coconut rum, banana liqueur, pineapple juice, and sweet and sour mix.",
        "Shake well until chilled.",
        "Strain into a tall glass filled with fresh ice.",
        "Garnish with a pineapple wedge or cherry.",
    ],
},
{
    "name": "Blue Iguana",
    "category": "Cocktails",
    "description": "A bright tropical blue cocktail with coconut rum, blue curaçao, pineapple, and citrus.",
    "emoji": "🦎",
    "strength": "Medium",
    "vibe": "Beachy",
    "tags": ["Blue Curaçao", "Coconut", "Pineapple", "Tropical"],
    "flavor": "Fruity",
    "image": "images/blue_iguana.jpg",
    "ingredients": [
        "1 oz coconut rum",
        "1 oz blue curaçao",
        "2 oz pineapple juice",
        "1 oz lemon-lime soda",
        "Ice",
        "Pineapple wedge or cherry for garnish",
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add coconut rum, blue curaçao, and pineapple juice.",
        "Shake until chilled.",
        "Pour into a glass filled with fresh ice.",
        "Top with lemon-lime soda.",
        "Garnish with a pineapple wedge or cherry.",
    ],
},
{
    "name": "Key Lime Pie Crush",
    "category": "Cocktails",
    "description": "A creamy tropical cocktail with coconut rum, vanilla vodka, pineapple, and key lime flavors.",
    "emoji": "🥧",
    "strength": "Medium",
    "vibe": "Dessert",
    "tags": ["Key Lime", "Coconut", "Creamy", "Sweet"],
    "flavor": "Dessert",
    "image": "images/key_lime_pie_crush.jpg",
    "ingredients": [
        "1 oz vanilla vodka",
        "1 oz coconut rum",
        "2 oz pineapple juice",
        "1 oz key lime juice",
        "1 oz cream of coconut",
        "Ice",
        "Whipped cream for garnish",
        "Lime wedge or graham cracker crumbs for garnish",
    ],
    "recipe": [
        "Fill a cocktail shaker with ice.",
        "Add vanilla vodka, coconut rum, pineapple juice, key lime juice, and cream of coconut.",
        "Shake well until cold and creamy.",
        "Pour into a glass filled with fresh ice.",
        "Top with whipped cream if desired.",
        "Garnish with a lime wedge or graham cracker crumbs.",
    ],
},
    {
        "name": "Campfire Old Fashioned",
        "category": "Cocktails",
        "description": "Bourbon, bitters, orange, and smoky campfire sweetness.",
        "emoji": "🥃",
        "strength": "Strong",
        "vibe": "Cozy",
        "tags": ["Bourbon", "Classic", "Campfire"],
        "flavor": "Smoky / Classic",
        "ingredients": [
            "2 oz bourbon",
            "2 dashes bitters",
            "1 sugar cube or 1/2 oz simple syrup",
            "Orange peel",
            "Large ice cube",
        ],
        "recipe": [
            "Add sugar and bitters to a glass.",
            "Add bourbon and stir with ice.",
            "Garnish with orange peel.",
            "Optional: smoke the glass for campfire flavor.",
        ],
    },
    {
        "name": "Lake House Mule",
        "category": "Cocktails",
        "description": "Vodka, ginger beer, lime, and mint over ice.",
        "emoji": "🍋",
        "strength": "Medium",
        "vibe": "Refreshing",
        "tags": ["Vodka", "Ginger", "Crisp"],
        "flavor": "Refreshing",
        "ingredients": [
            "2 oz vodka",
            "1/2 oz lime juice",
            "Ginger beer",
            "Mint",
            "Ice",
        ],
        "recipe": [
            "Fill glass with ice.",
            "Add vodka and lime juice.",
            "Top with ginger beer.",
            "Garnish with mint and lime.",
        ],
    },
    {
        "name": "Tipsy Camper Punch",
        "category": "Cocktails",
        "description": "Rum, pineapple, orange, and grenadine.",
        "emoji": "🌴",
        "strength": "Medium",
        "vibe": "Tropical",
        "tags": ["Rum", "Pineapple", "Sweet"],
        "flavor": "Fruity",
        "ingredients": [
            "2 oz rum",
            "3 oz pineapple juice",
            "2 oz orange juice",
            "Splash of grenadine",
            "Ice",
        ],
        "recipe": [
            "Add rum and juices to a shaker with ice.",
            "Shake well.",
            "Pour into glass.",
            "Add grenadine and let it settle.",
        ],
    },
    {
    "name": "Gummy Bear Shot",
    "category": "Shots",
    "description": "A sweet fruity shot with peach, raspberry, and citrus flavors that tastes like gummy candy.",
    "emoji": "🧸",
    "strength": "Medium",
    "vibe": "Party",
    "tags": ["Peach", "Raspberry", "Sweet", "Candy"],
    "flavor": "Fruity",
    "image": "images/gummy_bear_shot.jpg",
    "ingredients": [
        "1 oz raspberry liqueur",
        "1 oz peach schnapps",
        "Splash of lemon-lime soda",
        "Ice",
        "Optional gummy bear garnish",
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add raspberry liqueur and peach schnapps.",
        "Shake until chilled.",
        "Strain into shot glasses.",
        "Top with a splash of lemon-lime soda.",
        "Optional: garnish with gummy bears.",
    ],
},
    {
    "name": "Peach Ring Royal",
    "category": "Cocktails",
    "description": "A sweet peach cocktail with Crown Royal Peach, peach rings, and citrus soda.",
    "emoji": "🍑",
    "strength": "Medium",
    "vibe": "Party",
    "tags": ["Peach", "Whiskey", "Candy", "Sweet"],
    "flavor": "Fruity",
    "image": "images/peach_ring_royal.jpg",
    "ingredients": [
        "2 oz Crown Royal Peach",
        "4 oz lemon-lime soda",
        "Splash of peach juice",
        "Ice",
        "Peach ring candies for garnish",
    ],
    "recipe": [
        "Fill a glass with ice.",
        "Add Crown Royal Peach.",
        "Top with lemon-lime soda and a splash of peach juice.",
        "Stir gently to combine.",
        "Garnish with peach ring candies.",
    ],
},
    {
    "name": "Berries & Bubbles",
    "category": "Cocktails",
    "description": "A sparkling berry cocktail with vodka, berries, and prosecco for a light elegant sip.",
    "emoji": "🫧",
    "strength": "Light",
    "vibe": "Elegant",
    "tags": ["Berries", "Prosecco", "Sparkling", "Refreshing"],
    "flavor": "Fruity",
    "image": "images/berries_and_bubbles.jpg",
    "ingredients": [
        "1 oz vodka",
        "1 oz mixed berry purée or berry syrup",
        "4 oz prosecco or sparkling wine",
        "Fresh berries",
        "Ice",
        "Mint for garnish",
    ],
    "recipe": [
        "Add berry purée and vodka to a shaker with ice.",
        "Shake lightly until chilled.",
        "Strain into a wine glass or champagne flute.",
        "Top with chilled prosecco.",
        "Garnish with fresh berries and mint.",
        "Serve immediately while bubbly.",
    ],
},
    {
    "name": "Liquid Marijuana Shot",
    "category": "Shots",
    "description": "A tropical green shot with coconut, melon, pineapple, and citrus flavors.",
    "emoji": "🌴",
    "strength": "Medium",
    "vibe": "Party",
    "tags": ["Melon", "Coconut", "Pineapple", "Tropical"],
    "flavor": "Fruity",
    "image": "images/liquid_marijuana_shot.jpg",
    "ingredients": [
        "1/2 oz coconut rum",
        "1/2 oz spiced rum",
        "1/2 oz Midori melon liqueur",
        "1/2 oz blue curaçao",
        "Splash pineapple juice",
        "Ice",
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add coconut rum, spiced rum, Midori, blue curaçao, and pineapple juice.",
        "Shake well until chilled.",
        "Strain into shot glasses.",
        "Serve immediately cold.",
    ],
},
    {
    "name": "Green Tea Shot",
    "category": "Shots",
    "description": "A smooth whiskey shot with peach schnapps and citrus that tastes surprisingly like green tea.",
    "emoji": "🍵",
    "strength": "Medium",
    "vibe": "Party",
    "tags": ["Whiskey", "Peach", "Citrus", "Sweet"],
    "flavor": "Refreshing",
    "image": "images/green_tea_shot.jpg",
    "ingredients": [
        "1/2 oz Irish whiskey",
        "1/2 oz peach schnapps",
        "Splash sweet and sour mix",
        "Splash lemon-lime soda",
        "Ice",
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add Irish whiskey, peach schnapps, and sweet and sour mix.",
        "Shake until chilled.",
        "Strain into shot glasses.",
        "Top with a splash of lemon-lime soda.",
        "Serve immediately.",
    ],
},
    {
    "name": "Peanut Butter & Jelly Shot",
    "category": "Shots",
    "description": "A sweet candy-like shot with peanut butter whiskey and raspberry flavors.",
    "emoji": "🥜",
    "strength": "Medium",
    "vibe": "Fun",
    "tags": ["Peanut Butter", "Raspberry", "Sweet", "Candy"],
    "flavor": "Dessert",
    "image": "images/pbj_shot.jpg",
    "ingredients": [
        "1 oz peanut butter whiskey",
        "1 oz raspberry liqueur or Chambord",
        "Ice",
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add peanut butter whiskey and raspberry liqueur.",
        "Shake until chilled.",
        "Strain into shot glasses.",
        "Serve immediately.",
    ],
},
    
    {
    "name": "Pineapple Upside-Down Cake Shot",
    "category": "Shots",
    "description": "A sweet fruity shot that tastes like pineapple upside-down cake with hints of vanilla and cherry.",
    "emoji": "🍍",
    "strength": "Medium",
    "vibe": "Dessert",
    "tags": ["Pineapple", "Vanilla", "Cake", "Sweet"],
    "flavor": "Dessert",
    "image": "images/pineapple_upside_down_cake_shot.jpg",
    "ingredients": [
        "1 oz vanilla vodka",
        "1 oz pineapple juice",
        "Splash grenadine",
        "Ice",
        "Optional cherry garnish",
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add vanilla vodka and pineapple juice.",
        "Shake until chilled.",
        "Strain into shot glasses.",
        "Add a splash of grenadine to each shot.",
        "Optional: garnish with a cherry.",
    ],
},
    {
    "name": "Johnny Vegas Shot",
    "category": "Shots",
    "description": "A sweet and fruity party shot with watermelon flavor, tequila kick, and a splash of energy drink.",
    "emoji": "🎰",
    "strength": "Strong",
    "vibe": "Party",
    "tags": ["Watermelon", "Tequila", "Energy Drink", "Sweet"],
    "flavor": "Fruity",
    "image": "images/johnny_vegas_shot.jpg",
    "ingredients": [
        "1 oz tequila",
        "1 oz watermelon schnapps or watermelon pucker",
        "Splash Red Bull",
        "Ice"
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add tequila and watermelon schnapps.",
        "Shake until chilled.",
        "Strain into shot glasses.",
        "Top with a splash of Red Bull.",
        "Serve immediately."
    ]
},
    {
    "name": "Scooby Snack Shot",
    "category": "Shots",
    "description": "A creamy tropical shot with coconut, banana, melon, and pineapple flavors that tastes like a fun vacation dessert drink.",
    "emoji": "💚",
    "strength": "Medium",
    "vibe": "Tropical",
    "tags": ["Coconut", "Banana", "Melon", "Creamy", "Pineapple"],
    "flavor": "Creamy",
    "image": "images/scooby_snack_shot.jpg",
    "ingredients": [
        "1/2 oz coconut rum",
        "1/2 oz melon liqueur",
        "1/2 oz banana liqueur",
        "1/2 oz pineapple juice",
        "1/4 oz heavy cream",
        "Ice",
        "Optional whipped cream garnish"
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add coconut rum, melon liqueur, banana liqueur, pineapple juice, and heavy cream.",
        "Shake until smooth and chilled.",
        "Strain into shot glasses.",
        "Optional: top with whipped cream.",
        "Serve immediately."
    ]
},
    {
    "name": "Berry Bomb",
    "category": "Cocktails",
    "description": "A sweet berry cocktail with watermelon and citrus flavors balanced by Wild Berry Red Bull.",
    "emoji": "💣",
    "strength": "Strong",
    "vibe": "Nightlife",
    "tags": ["Berry", "Watermelon", "Party", "Sweet"],
    "flavor": "Fruity",
    "image": "images/berry_bomb.jpg",
    "ingredients": [
        "1 oz vodka",
        "1 oz watermelon pucker",
        "1/2 oz raspberry liqueur",
        "1 can Red Bull Wild Berry",
        "Ice"
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add vodka, watermelon pucker, and raspberry liqueur.",
        "Shake until chilled.",
        "Pour into a glass with fresh ice.",
        "Top with Red Bull Wild Berry.",
        "Serve immediately."
    ]
},
    {
    "name": "Caramel Apple Cider Mule",
    "category": "Cocktails",
    "description": "A cozy fall cocktail with apple cider, caramel vodka, ginger beer, and warm spice flavors.",
    "emoji": "🍎",
    "strength": "Medium",
    "vibe": "Campfire",
    "tags": ["Apple Cider", "Fall", "Caramel", "Ginger Beer", "Cozy"],
    "flavor": "Spiced",
    "image": "images/caramel_apple_cider_mule.jpg",
    "ingredients": [
        "2 oz caramel vodka",
        "3 oz apple cider",
        "4 oz ginger beer",
        "Ice",
        "Optional apple slices",
        "Optional cinnamon stick garnish"
    ],
    "recipe": [
        "Fill a mule mug or glass with ice.",
        "Add caramel vodka and apple cider.",
        "Top with ginger beer.",
        "Stir gently.",
        "Optional: garnish with apple slices and a cinnamon stick.",
        "Serve immediately."
    ]
},
{
    "name": "Cinnamon Whiskey Cider",
    "category": "Cocktails",
    "description": "A warm and smooth whiskey cocktail with crisp apple cider and cinnamon spice.",
    "emoji": "🥃",
    "strength": "Strong",
    "vibe": "Bonfire",
    "tags": ["Whiskey", "Apple Cider", "Cinnamon", "Fall", "Warm"],
    "flavor": "Spiced",
    "image": "images/cinnamon_whiskey_cider.jpg",
    "ingredients": [
        "2 oz cinnamon whiskey",
        "4 oz apple cider",
        "Ice",
        "Optional apple slice garnish",
        "Optional cinnamon sugar rim"
    ],
    "recipe": [
        "Fill a glass with ice.",
        "Add cinnamon whiskey.",
        "Pour in apple cider.",
        "Stir gently until chilled.",
        "Optional: garnish with apple slices.",
        "Serve immediately."
    ]
},
{
    "name": "Apple Pie Martini",
    "category": "Cocktails",
    "description": "A sweet dessert cocktail that tastes like fresh apple pie with cinnamon and vanilla notes.",
    "emoji": "🥧",
    "strength": "Medium",
    "vibe": "Dessert",
    "tags": ["Apple", "Vanilla", "Cinnamon", "Dessert", "Fall"],
    "flavor": "Dessert",
    "image": "images/apple_pie_martini.jpg",
    "ingredients": [
        "2 oz vanilla vodka",
        "2 oz apple cider",
        "1 oz cinnamon schnapps",
        "Ice",
        "Optional cinnamon sugar rim"
    ],
    "recipe": [
        "Optional: rim the martini glass with cinnamon sugar.",
        "Fill a shaker with ice.",
        "Add vanilla vodka, apple cider, and cinnamon schnapps.",
        "Shake until chilled.",
        "Strain into a martini glass.",
        "Serve immediately."
    ]
},
    {
    "name": "Butter Baby",
    "category": "Shots",
    "description": "A rich and sweet dessert-style shot with butterscotch, coconut, coffee, and creamy flavors.",
    "emoji": "🧈",
    "strength": "Medium",
    "vibe": "Dessert",
    "tags": ["Butterscotch", "Creamy", "Coffee", "Sweet", "Coconut"],
    "flavor": "Dessert",
    "image": "images/butter_baby.jpg",
    "ingredients": [
        "1 oz butterscotch schnapps",
        "1/2 oz amaretto",
        "1/2 oz Kahlúa",
        "1/4 oz coconut rum",
        "Splash milk",
        "Ice"
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add butterscotch schnapps, amaretto, Kahlúa, coconut rum, and milk.",
        "Shake until chilled and creamy.",
        "Strain into a shot glass.",
        "Serve immediately."
    ]
},
    {
    "name": "Mini Beer Shot",
    "category": "Shots",
    "description": "A fun layered shot that looks like a tiny glass of beer with sweet vanilla and creamy flavors.",
    "emoji": "🍺",
    "strength": "Medium",
    "vibe": "Fun",
    "tags": ["Vanilla", "Creamy", "Layered", "Party", "Sweet"],
    "flavor": "Dessert",
    "image": "images/mini_beer_shot.jpg",
    "ingredients": [
        "1 1/2 oz Licor 43",
        "1/2 oz heavy cream"
    ],
    "recipe": [
        "Pour Licor 43 into a shot glass.",
        "Slowly float heavy cream on top using the back of a spoon.",
        "Serve immediately."
    ]
},
    {
    "name": "Fresh Blackberry Margarita",
    "category": "Margaritas",
    "description": "A refreshing berry margarita made with muddled blackberries, tequila, lime, and orange liqueur for the perfect summer cocktail.",
    "emoji": "🫐",
    "strength": "Medium",
    "vibe": "Summer",
    "tags": ["Blackberry", "Tequila", "Fresh", "Citrus", "Berry"],
    "flavor": "Fruity",
    "image": "images/fresh_blackberry_margarita.jpg",
    "ingredients": [
        "1/4 cup fresh blackberries",
        "1/2 oz simple syrup",
        "2 oz reposado tequila",
        "1 oz orange liqueur",
        "1 oz fresh lime juice",
        "Ice",
        "Optional lime garnish",
        "Optional salt rim"
    ],
    "recipe": [
        "Add blackberries and simple syrup to a cocktail shaker.",
        "Muddle until the berries are fully broken down.",
        "Add tequila, orange liqueur, lime juice, and ice.",
        "Shake vigorously until chilled.",
        "Optional: rim the glass with lime and salt.",
        "Strain into a glass filled with fresh ice.",
        "Garnish with blackberries or a lime wedge if desired."
    ]
},
    {
    "name": "Bullfrog",
    "category": "Cocktails",
    "description": "A powerful neon-green party cocktail packed with multiple liquors and an energy drink kick.",
    "emoji": "🐸",
    "strength": "Very Strong",
    "vibe": "Party",
    "tags": ["Blue Curacao", "Energy Drink", "Strong", "Party", "Citrus"],
    "flavor": "Citrus",
    "image": "images/bullfrog.jpg",
    "ingredients": [
        "1 oz vodka",
        "1 oz white rum",
        "1 oz gin",
        "1 oz tequila",
        "1 oz triple sec",
        "1/2 oz blue curaçao",
        "Red Bull or other energy drink",
        "Ice"
    ],
    "recipe": [
        "Fill a pint glass with ice.",
        "Add vodka, white rum, gin, tequila, triple sec, and blue curaçao.",
        "Top with Red Bull.",
        "Stir gently until combined.",
        "Serve immediately."
    ]
},
    
    {
    "name": "Applebee’s Perfect Margarita",
    "category": "Margaritas",
    "description": "A bold citrus margarita with tequila, Grand Marnier, and fresh lime flavor.",
    "emoji": "🍹",
    "strength": "Medium",
    "vibe": "Restaurant Favorite",
    "tags": ["Tequila", "Grand Marnier", "Citrus", "Classic"],
    "flavor": "Lemon / Citrus",
    "image": "images/applebees_perfect_margarita.jpg",
    "ingredients": [
        "1 1/4 oz tequila",
        "1/2 oz triple sec",
        "1/2 oz Grand Marnier",
        "1 1/2 oz freshly squeezed lime juice",
        "4 oz prepared sweet-and-sour mix",
        "1/2 oz simple syrup",
        "Ice",
        "Salt for rim",
        "Lime wedge for garnish",
    ],
    "recipe": [
        "Rim a margarita glass with salt.",
        "Fill a shaker with ice.",
        "Add tequila, triple sec, Grand Marnier, lime juice, sweet-and-sour mix, and simple syrup.",
        "Shake well until chilled.",
        "Pour into a glass filled with fresh ice.",
        "Garnish with a lime wedge.",
    ],
},
    {
    "name": "Grape Tootsie Roll Shot",
    "category": "Shots",
    "description": "A sweet grape candy shot with chocolatey Tootsie Roll flavor and a splash of citrus.",
    "emoji": "🍇",
    "strength": "Medium",
    "vibe": "Candy",
    "tags": ["Grape", "Chocolate", "Orange", "Sweet"],
    "flavor": "Dessert",
    "image": "images/grape_tootsie_roll_shot.jpg",
    "ingredients": [
        "1 oz coffee liqueur",
        "1 oz grape vodka or grape liqueur",
        "Splash orange juice",
        "Ice",
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add coffee liqueur, grape vodka, and orange juice.",
        "Shake until chilled.",
        "Strain into shot glasses.",
        "Serve immediately cold.",
    ],
},
    {
    "name": "Mai Tai",
    "category": "Cocktails",
    "description": "A tropical rum cocktail with lime, orange, and island flavors.",
    "emoji": "🌴",
    "strength": "Strong",
    "vibe": "Beachy",
    "tags": ["Rum", "Tropical", "Lime", "Island"],
    "flavor": "Fruity",
    "image": "images/mai_tai.jpg",
    "ingredients": [
        "2 oz dark rum",
        "1 oz orange curaçao",
        "1 oz lime juice",
        "1/2 oz orgeat syrup",
        "Ice",
        "Mint sprig for garnish",
        "Lime wheel or cherry for garnish",
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add rum, orange curaçao, lime juice, and orgeat syrup.",
        "Shake well until chilled.",
        "Pour into a glass filled with crushed ice.",
        "Garnish with mint, lime, or a cherry.",
        "Serve immediately.",
    ],
},
    {
    "name": "Bahama Mama",
    "category": "Cocktails",
    "description": "A tropical rum cocktail with pineapple, orange, coconut, and grenadine flavors.",
    "emoji": "🌺",
    "strength": "Medium",
    "vibe": "Tropical",
    "tags": ["Rum", "Pineapple", "Coconut", "Beachy"],
    "flavor": "Fruity",
    "image": "images/bahama_mama.jpg",
    "ingredients": [
        "1 oz coconut rum",
        "1 oz dark rum",
        "2 oz pineapple juice",
        "1 oz orange juice",
        "Splash grenadine",
        "Ice",
        "Orange slice or cherry for garnish",
    ],
    "recipe": [
        "Fill a shaker with ice.",
        "Add coconut rum, dark rum, pineapple juice, and orange juice.",
        "Shake until chilled.",
        "Pour into a glass filled with fresh ice.",
        "Add a splash of grenadine.",
        "Garnish with an orange slice or cherry.",
    ],
},
    {
        "name": "Campfire Shot",
        "category": "Shots",
        "description": "Whiskey and cinnamon with a warm kick.",
        "emoji": "🔥",
        "strength": "Strong",
        "vibe": "Bold",
        "tags": ["Whiskey", "Cinnamon"],
        "flavor": "Smoky / Classic",
        "ingredients": [
            "1 oz whiskey",
            "1/2 oz cinnamon whiskey",
        ],
        "recipe": [
            "Pour both into a shaker with ice.",
            "Shake briefly.",
            "Strain into shot glass.",
        ],
    },
    {
        "name": "Pineapple Pit Stop",
        "category": "Shots",
        "description": "Pineapple vodka with lime.",
        "emoji": "🍍",
        "strength": "Medium",
        "vibe": "Fun",
        "tags": ["Vodka", "Pineapple"],
        "flavor": "Fruity",
        "ingredients": [
            "1 oz pineapple vodka",
            "Splash of lime juice",
            "Optional sugar rim",
        ],
        "recipe": [
            "Shake vodka and lime with ice.",
            "Strain into shot glass.",
            "Serve cold.",
        ],
    },
    {
        "name": "Campground Margarita",
        "category": "Margaritas",
        "description": "Classic tequila, lime, and orange liqueur.",
        "emoji": "🍹",
        "strength": "Medium",
        "vibe": "Classic",
        "tags": ["Tequila", "Lime"],
        "flavor": "Lemon / Citrus",
        "ingredients": [
            "2 oz tequila",
            "1 oz lime juice",
            "1 oz orange liqueur",
            "1/2 oz simple syrup",
            "Salt rim",
        ],
        "recipe": [
            "Rim glass with salt.",
            "Shake tequila, lime, orange liqueur, and syrup with ice.",
            "Pour over fresh ice.",
            "Garnish with lime.",
        ],
    },
    {
        "name": "Pineapple Camper Rita",
        "category": "Margaritas",
        "description": "Pineapple margarita with tajin rim.",
        "emoji": "🍍",
        "strength": "Medium",
        "vibe": "Tropical",
        "tags": ["Pineapple", "Tajin"],
        "flavor": "Fruity",
        "ingredients": [
            "2 oz tequila",
            "2 oz pineapple juice",
            "1 oz lime juice",
            "1 oz orange liqueur",
            "Tajin rim",
        ],
        "recipe": [
            "Rim glass with tajin.",
            "Shake all ingredients with ice.",
            "Pour over ice.",
            "Garnish with pineapple or lime.",
        ],
    },
    {
        "name": "Jalapeño Camp Rita",
        "category": "Margaritas",
        "description": "Spicy jalapeño margarita with fresh citrus.",
        "emoji": "🔥",
        "strength": "Strong",
        "vibe": "Spicy",
        "tags": ["Jalapeño", "Tequila"],
        "flavor": "Spicy",
        "ingredients": [
            "2 oz tequila",
            "1 oz lime juice",
            "1 oz orange liqueur",
            "2 jalapeño slices",
            "Tajin or salt rim",
        ],
        "recipe": [
            "Muddle jalapeño in shaker.",
            "Add tequila, lime, orange liqueur, and ice.",
            "Shake well.",
            "Strain over ice.",
        ],
    },
    {
        "name": "Lake Day Lemonade",
        "category": "Camp Favorites",
        "description": "Vodka lemonade with strawberry splash.",
        "emoji": "🍋",
        "strength": "Light",
        "vibe": "Summer",
        "tags": ["Vodka", "Lemonade"],
        "flavor": "Lemon / Citrus",
        "ingredients": [
            "1.5 oz vodka",
            "Lemonade",
            "Strawberry puree or syrup",
            "Ice",
        ],
        "recipe": [
            "Fill glass with ice.",
            "Add vodka.",
            "Top with lemonade.",
            "Add strawberry splash and stir.",
        ],
    },
    {
        "name": "Bonfire Mule",
        "category": "Camp Favorites",
        "description": "Vodka, ginger beer, and lime.",
        "emoji": "🔥",
        "strength": "Medium",
        "vibe": "Cold",
        "tags": ["Vodka", "Lime"],
        "flavor": "Refreshing",
        "ingredients": [
            "2 oz vodka",
            "1/2 oz lime juice",
            "Ginger beer",
            "Ice",
        ],
        "recipe": [
            "Fill glass with ice.",
            "Add vodka and lime.",
            "Top with ginger beer.",
            "Stir and serve cold.",
        ],
    },
    {
        "name": "Camper Light",
        "category": "Beer & Seltzers",
        "description": "Cold domestic beer.",
        "emoji": "🍺",
        "strength": "Light",
        "vibe": "Easy",
        "tags": ["Beer"],
        "flavor": "Refreshing",
        "ingredients": [
            "1 cold domestic beer",
        ],
        "recipe": [
            "Open.",
            "Serve cold.",
            "Enjoy by the fire.",
        ],
    },
    {
        "name": "Lake Water Seltzer",
        "category": "Beer & Seltzers",
        "description": "Rotating hard seltzer flavors.",
        "emoji": "🫧",
        "strength": "Light",
        "vibe": "Refreshing",
        "tags": ["Seltzer"],
        "flavor": "Refreshing",
        "ingredients": [
            "1 hard seltzer",
            "Optional lime wedge",
        ],
        "recipe": [
            "Serve cold over ice or straight from the can.",
            "Add lime if desired.",
        ],
    },
    {
        "name": "Designated Camper",
        "category": "Mocktails",
        "description": "Pineapple, lime, soda water, and tajin.",
        "emoji": "🏕️",
        "strength": "None",
        "vibe": "Fresh",
        "tags": ["Mocktail"],
        "flavor": "Refreshing",
        "ingredients": [
            "3 oz pineapple juice",
            "1 oz lime juice",
            "Soda water",
            "Tajin rim",
            "Ice",
        ],
        "recipe": [
            "Rim glass with tajin.",
            "Add pineapple and lime over ice.",
            "Top with soda water.",
            "Stir gently.",
        ],
    },
]

df = pd.DataFrame(drinks)

category_order = [
    "Cocktails",
    "Shots",
    "Margaritas",
    "Camp Favorites",
    "Beer & Seltzers",
    "Mocktails",
]


# ============================================
# QUICK FILTER STATE
# ============================================

if "quick_category" not in st.session_state:
    st.session_state.quick_category = "All Drinks"

if "quick_strength" not in st.session_state:
    st.session_state.quick_strength = "All"

if "quick_flavor" not in st.session_state:
    st.session_state.quick_flavor = "All"

if "random_drink" not in st.session_state:
    st.session_state.random_drink = None


# ============================================
# CSS
# ============================================

st.markdown(
    f"""
<style>

.stApp {{
    background:
        radial-gradient(circle at top left, rgba(177, 116, 64, 0.18), transparent 34%),
        radial-gradient(circle at top right, rgba(51, 82, 65, 0.22), transparent 30%),
        linear-gradient(135deg, #050706 0%, #0B1210 38%, #15100B 100%);
    color: #F4E8D0;
    font-family: "Inter", "Segoe UI", sans-serif;
}}

.block-container {{
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1350px;
}}

.hero-section {{
    {hero_background}
    position: relative;
    overflow: hidden;
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    border-radius: 36px;
    padding: 135px 44px;
    margin-bottom: 38px;
    text-align: center;
    box-shadow:
        0 28px 80px rgba(0,0,0,0.68),
        inset 0 0 80px rgba(0,0,0,0.35);
    border: 1px solid rgba(217, 174, 110, 0.28);
}}

.hero-section::before {{
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(
            135deg,
            rgba(5, 7, 6, 0.04),
            rgba(5, 7, 6, 0.16)
        );
    backdrop-filter: blur(0px);
    z-index: 0;
}}

.hero-section::after {{
    content: "";
    position: absolute;
    width: 520px;
    height: 520px;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -45%);
    background: radial-gradient(circle, rgba(255, 188, 94, 0.14), transparent 62%);
    z-index: 0;
}}

.hero-title,
.hero-subtitle {{
    position: relative;
    z-index: 1;
}}

.hero-title {{
    font-size: 82px;
    line-height: 0.95;
    font-weight: 950;
    letter-spacing: -2.5px;
    color: #F8E3B0;
    text-shadow:
        0px 4px 12px rgba(0,0,0,0.78),
        0px 0px 34px rgba(224, 154, 80, 0.35);
    margin-bottom: 16px;
}}

.hero-subtitle {{
    display: inline-block;
    font-size: 22px;
    font-weight: 500;
    letter-spacing: 0.5px;
    color: #F6EFE2;
    background: rgba(8, 12, 10, 0.52);
    border: 1px solid rgba(217, 174, 110, 0.22);
    border-radius: 999px;
    padding: 12px 22px;
    box-shadow:
        0 10px 30px rgba(0,0,0,0.35),
        inset 0 1px 0 rgba(255,255,255,0.08);
}}

section[data-testid="stSidebar"] {{
    background:
        linear-gradient(180deg, #090F0D 0%, #0F1813 54%, #120D09 100%);
    border-right: 1px solid rgba(217, 174, 110, 0.16);
    box-shadow: 18px 0 45px rgba(0,0,0,0.34);
}}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {{
    color: #F8E3B0 !important;
    letter-spacing: -0.5px;
}}

section[data-testid="stSidebar"] label {{
    color: #D6C7AA !important;
    font-weight: 700 !important;
    font-size: 13px !important;
    letter-spacing: 0.3px;
}}

section[data-testid="stSidebar"] input,
section[data-testid="stSidebar"] div[data-baseweb="select"] > div {{
    background-color: rgba(244, 232, 208, 0.08) !important;
    border: 1px solid rgba(217, 174, 110, 0.20) !important;
    border-radius: 14px !important;
    color: #F4E8D0 !important;
}}

/* ============================================
   QUICK FILTER CARDS
============================================ */

.quick-filter-title {{
    color: #F8E3B0;
    font-size: 30px;
    font-weight: 950;
    letter-spacing: -0.9px;
    margin-bottom: 6px;
}}

.quick-filter-subtitle {{
    color: #BFAF92;
    font-size: 14px;
    margin-bottom: 20px;
}}

.quick-card {{
    min-height: 178px;
    background:
        linear-gradient(
            145deg,
            rgba(31, 49, 39, 0.94),
            rgba(14, 18, 15, 0.98)
        );
    border: 1px solid rgba(217, 174, 110, 0.24);
    border-radius: 28px;
    padding: 24px 20px;
    margin-bottom: 12px;
    text-align: center;
    box-shadow:
        0 18px 45px rgba(0,0,0,0.40),
        inset 0 1px 0 rgba(255,255,255,0.06);
}}

.quick-card:hover {{
    border-color: rgba(238, 194, 125, 0.45);
    box-shadow:
        0 24px 65px rgba(0,0,0,0.52),
        0 0 30px rgba(238, 194, 125, 0.08),
        inset 0 1px 0 rgba(255,255,255,0.08);
    transform: translateY(-2px);
    transition: all 0.22s ease;
}}

.quick-icon {{
    font-size: 40px;
    margin-bottom: 10px;
}}

.quick-title {{
    color: #F8E3B0;
    font-size: 20px;
    font-weight: 900;
    margin-bottom: 8px;
}}

.quick-subtitle {{
    color: #CFC2A8;
    font-size: 13px;
    line-height: 1.45;
}}

div.stButton > button {{
    background:
        linear-gradient(
            135deg,
            rgba(104, 78, 48, 0.95),
            rgba(37, 67, 50, 0.95)
        );
    color: #F9EBD1;
    border: 1px solid rgba(238, 194, 125, 0.35);
    border-radius: 999px;
    padding: 0.6rem 1rem;
    font-weight: 800;
    letter-spacing: 0.2px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}}

div.stButton > button:hover {{
    border-color: rgba(238, 194, 125, 0.75);
    color: #FFD99A;
    box-shadow:
        0 16px 35px rgba(0,0,0,0.35),
        0 0 22px rgba(238, 194, 125, 0.10);
}}

.section-title {{
    position: relative;
    font-size: 36px;
    font-weight: 900;
    color: #F8E3B0;
    margin-top: 52px;
    margin-bottom: 24px;
    letter-spacing: -1.2px;
}}

.section-title::after {{
    content: "";
    display: block;
    width: 100%;
    height: 1px;
    margin-top: 14px;
    background:
        linear-gradient(
            90deg,
            rgba(238, 194, 125, 0.75),
            rgba(238, 194, 125, 0.12),
            transparent
        );
}}

div[data-testid="stExpander"] {{
    background:
        linear-gradient(
            145deg,
            rgba(28, 42, 34, 0.96),
            rgba(13, 18, 15, 0.98)
        ) !important;
    border: 1px solid rgba(217, 174, 110, 0.20) !important;
    border-radius: 28px !important;
    margin-bottom: 24px !important;
    box-shadow:
        0 20px 55px rgba(0,0,0,0.44),
        inset 0 1px 0 rgba(255,255,255,0.06);
    overflow: hidden;
}}

div[data-testid="stExpander"]:hover {{
    border-color: rgba(238, 194, 125, 0.42) !important;
    box-shadow:
        0 26px 70px rgba(0,0,0,0.55),
        0 0 34px rgba(238, 194, 125, 0.08),
        inset 0 1px 0 rgba(255,255,255,0.08);
    transform: translateY(-2px);
    transition: all 0.22s ease;
}}

div[data-testid="stExpander"] summary {{
    padding: 20px 24px !important;
    font-size: 20px !important;
    font-weight: 850 !important;
    color: #F8E3B0 !important;
    letter-spacing: -0.3px;
}}

div[data-testid="stExpander"] summary:hover {{
    color: #FFD99A !important;
}}

.drink-card {{
    background:
        linear-gradient(
            145deg,
            rgba(49, 70, 54, 0.42),
            rgba(9, 13, 11, 0.24)
        );
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 18px;
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
}}

.drink-name {{
    font-size: 27px;
    font-weight: 900;
    color: #F8E3B0;
    letter-spacing: -0.6px;
}}

.drink-description {{
    font-size: 15.5px;
    color: #E7DAC1;
    margin-top: 12px;
    line-height: 1.65;
}}

.pill {{
    display: inline-block;
    background:
        linear-gradient(
            135deg,
            rgba(104, 78, 48, 0.65),
            rgba(37, 67, 50, 0.70)
        );
    color: #F9EBD1;
    border: 1px solid rgba(238, 194, 125, 0.22);
    padding: 7px 12px;
    border-radius: 999px;
    margin-right: 8px;
    margin-bottom: 8px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.2px;
}}

.tag {{
    display: inline-block;
    background: rgba(244, 232, 208, 0.08);
    color: #D9C5A1;
    border: 1px solid rgba(217, 174, 110, 0.14);
    padding: 6px 11px;
    border-radius: 999px;
    margin-right: 7px;
    margin-top: 10px;
    font-size: 12px;
    font-weight: 650;
}}

.recipe-panel {{
    background:
        linear-gradient(
            145deg,
            rgba(10, 16, 13, 0.96),
            rgba(25, 20, 14, 0.92)
        );
    border-radius: 22px;
    border: 1px solid rgba(217, 174, 110, 0.22);
    padding: 20px 24px;
    margin-top: 18px;
    margin-bottom: 20px;
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.05),
        0 12px 30px rgba(0,0,0,0.25);
}}

.recipe-title {{
    color: #EEC27D;
    font-size: 18px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 10px;
}}

.recipe-list {{
    color: #E8DCC6;
    font-size: 15px;
    line-height: 1.6;
    margin-bottom: 16px;
}}

.recipe-list li {{
    margin-bottom: 6px;
}}

hr {{
    border: none;
    height: 1px;
    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(238, 194, 125, 0.38),
            transparent
        );
    margin-top: 42px;
}}

.footer {{
    text-align: center;
    color: #AFA38E;
    padding: 26px;
    font-size: 13px;
    letter-spacing: 0.6px;
}}

@media screen and (max-width: 900px) {{
    .hero-title {{
        font-size: 52px;
    }}

    .hero-subtitle {{
        font-size: 16px;
        border-radius: 18px;
    }}

    .hero-section {{
        padding: 90px 22px;
    }}

    .section-title {{
        font-size: 30px;
    }}

    .quick-card {{
        min-height: auto;
    }}
}}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================
# HERO
# ============================================

st.markdown(
    """
<div class="hero-section">
    <div class="hero-title">🍹 A Simple Bar</div>
    <div class="hero-subtitle">
        Margaritas: making bugs, smoke, and close neighbors tolerable.
    </div>
</div>
""",
    unsafe_allow_html=True,
)


# ============================================
# QUICK FILTER CARDS
# ============================================

st.markdown(
    """
<div class="quick-filter-title">Find Your Camp Drink</div>
<div class="quick-filter-subtitle">
    Choose wisely. The camper parking already tested your marriage.
</div>
""",
    unsafe_allow_html=True,
)

q1, q2, q3, q4 = st.columns(4)



with q1:
    st.markdown(
        """
<div class="quick-card">
    <div class="quick-icon">🍹</div>
    <div class="quick-title">All Drinks</div>
    <div class="quick-subtitle">Camp responsibly. Drink questionably.</div>
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button("Show All Drinks", use_container_width=True):
        st.session_state.quick_category = "All Drinks"
        st.session_state.quick_strength = "All"
        st.session_state.quick_flavor = "All"
    
        st.markdown(
            """
            <script>
                window.location.hash = "all";
            </script>
            """,
            unsafe_allow_html=True,
        )
    
        st.rerun()
        
with q2:
    st.markdown(
        """
<div class="quick-card">
    <div class="quick-icon">🍹</div>
    <div class="quick-title">Margaritas</div>
    <div class="quick-subtitle">Nature needs tequila.</div>
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button("Show Margaritas", use_container_width=True):
        st.session_state.quick_category = "Margaritas"
        st.session_state.quick_strength = "All"
        st.session_state.quick_flavor = "All"

        st.markdown(
            """
            <script>
                window.location.hash = "margaritas";
            </script>
            """,
            unsafe_allow_html=True,
        )

        st.rerun()

with q3:
    st.markdown(
        """
<div class="quick-card">
    <div class="quick-icon">🌴</div>
    <div class="quick-title">Fruity Drinks</div>
    <div class="quick-subtitle">Proof that pineapple can’t be trusted.</div>
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button("Show Fruity Drinks", use_container_width=True):
        st.session_state.quick_category = "All Drinks"
        st.session_state.quick_strength = "All"
        st.session_state.quick_flavor = "Fruity"
    
        st.markdown(
            """
            <script>
                window.location.hash = "fruity";
            </script>
            """,
            unsafe_allow_html=True,
        )
    
        st.rerun()

with q4:
    st.markdown(
        """
<div class="quick-card">
    <div class="quick-icon">🥃</div>
    <div class="quick-title">Shots</div>
    <div class="quick-subtitle">When the fire’s lit and so are you.</div>
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button("Show Shots", use_container_width=True):
        st.session_state.quick_category = "Shots"
        st.session_state.quick_strength = "All"
        st.session_state.quick_flavor = "All"
    
        st.markdown(
            """
            <script>
                window.location.hash = "shots";
            </script>
            """,
            unsafe_allow_html=True,
        )
    
        st.rerun()


# ============================================
# SIDEBAR
# ============================================

st.sidebar.markdown("## 🍻 Menu Controls")

search = st.sidebar.text_input("Search Drinks")

category_options = ["All Drinks"] + category_order
strength_options = ["All"] + sorted(df["strength"].unique().tolist())
flavor_options = ["All"] + sorted(df["flavor"].unique().tolist())

selected_category = st.sidebar.selectbox(
    "Category",
    category_options,
    index=category_options.index(st.session_state.quick_category),
)

selected_strength = st.sidebar.selectbox(
    "Drink Strength",
    strength_options,
    index=strength_options.index(st.session_state.quick_strength),
)

selected_flavor = st.sidebar.selectbox(
    "Flavor Profile",
    flavor_options,
    index=flavor_options.index(st.session_state.quick_flavor),
)

if st.sidebar.button("Clear Filters", use_container_width=True):
    st.session_state.quick_category = "All Drinks"
    st.session_state.quick_strength = "All"
    st.session_state.quick_flavor = "All"
    st.rerun()


# ============================================
# FILTERING
# ============================================

filtered_df = df.copy()

if selected_category != "All Drinks":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]

if selected_strength != "All":
    filtered_df = filtered_df[filtered_df["strength"] == selected_strength]

if selected_flavor != "All":
    filtered_df = filtered_df[filtered_df["flavor"] == selected_flavor]

if search:
    search_lower = search.lower()

    filtered_df = filtered_df[
        filtered_df["name"].str.lower().str.contains(search_lower, na=False)
        | filtered_df["description"].str.lower().str.contains(search_lower, na=False)
        | filtered_df["flavor"].str.lower().str.contains(search_lower, na=False)
        | filtered_df["tags"].apply(
            lambda tags: any(search_lower in tag.lower() for tag in tags)
        )
    ]

# ============================================
# RANDOM DRINK PICKER
# ============================================

st.markdown(
    """
<div class="quick-filter-title">Feeling Lucky?</div>
<div class="quick-filter-subtitle">
    Let the camp bartender pick something for you.
</div>
""",
    unsafe_allow_html=True,
)

random_col1, random_col2 = st.columns(2)

with random_col1:
    if st.button("🎲 Random Drink Picker", use_container_width=True):
        drink_df = df[df["category"] != "Shots"]

        if selected_strength != "All":
            drink_df = drink_df[drink_df["strength"] == selected_strength]

        if selected_flavor != "All":
            drink_df = drink_df[drink_df["flavor"] == selected_flavor]

        if not drink_df.empty:
            st.session_state.random_drink = drink_df.sample(1).iloc[0].to_dict()
        else:
            st.warning("No drinks match your current filters.")

with random_col2:
    if st.button("🥃 Random Shot", use_container_width=True):
        shot_df = df[df["category"] == "Shots"]

        if selected_strength != "All":
            shot_df = shot_df[shot_df["strength"] == selected_strength]

        if selected_flavor != "All":
            shot_df = shot_df[shot_df["flavor"] == selected_flavor]

        if not shot_df.empty:
            st.session_state.random_drink = shot_df.sample(1).iloc[0].to_dict()
        else:
            st.warning("No shots match your current filters.")

if st.session_state.random_drink is not None:
    picked = st.session_state.random_drink

    random_tags_html = "".join(
        [f'<span class="tag">{tag}</span>' for tag in picked["tags"]]
    )

    random_card_html = f"""
<div class="drink-card">
    <div class="drink-name">
        🎯 Tonight's Pick: {picked["emoji"]} {picked["name"]}
    </div>

    <div class="drink-description">
        {picked["description"]}
    </div>

    <div style="margin-top:14px;">
        <span class="pill">Strength: {picked["strength"]}</span>
        <span class="pill">Vibe: {picked["vibe"]}</span>
        <span class="pill">{picked["category"]}</span>
        <span class="pill">Flavor: {picked["flavor"]}</span>
    </div>

    <div style="margin-top:10px;">
        {random_tags_html}
    </div>
</div>
"""

    st.html(random_card_html)
# ============================================
# DRINK DISPLAY
# ============================================

if filtered_df.empty:
    st.warning("No drinks match your filters.")
else:
    for category in category_order:
        items = filtered_df[filtered_df["category"] == category]

        if items.empty:
            continue

section_id = category.lower().replace(" ", "-").replace("&", "and")

st.markdown(
    f'''
    <div id="{section_id}" class="section-title">
        {category}
    </div>
    ''',
    unsafe_allow_html=True,
)

        cols = st.columns(2)

        for i, (_, row) in enumerate(items.iterrows()):
            with cols[i % 2]:

                tags_html = "".join(
                    [f'<span class="tag">{tag}</span>' for tag in row["tags"]]
                )

                ingredients_html = "".join(
                    [f"<li>{ingredient}</li>" for ingredient in row["ingredients"]]
                )

                recipe_html = "".join(
                    [f"<li>{step}</li>" for step in row["recipe"]]
                )

                with st.expander(f'{row["emoji"]} {row["name"]}'):

                    card_html = f"""
<div class="drink-card">
    <div class="drink-name">
        {row["emoji"]} {row["name"]}
    </div>

    <div class="drink-description">
        {row["description"]}
    </div>

    <div style="margin-top:14px;">
        <span class="pill">Strength: {row["strength"]}</span>
        <span class="pill">Vibe: {row["vibe"]}</span>
        <span class="pill">{row["category"]}</span>
        <span class="pill">Flavor: {row["flavor"]}</span>
    </div>

    <div style="margin-top:10px;">
        {tags_html}
    </div>
</div>

<div class="recipe-panel">
    <div class="recipe-title">Ingredients</div>
    <ul class="recipe-list">
        {ingredients_html}
    </ul>

    <div class="recipe-title">How to Make It</div>
    <ol class="recipe-list">
        {recipe_html}
    </ol>
</div>
"""

                    st.html(card_html)


# ============================================
# FOOTER
# ============================================

st.markdown("---")

st.markdown(
    """
<div class="footer">
🏕️ A Simple Bar • Camping nights, margaritas, and questionable decisions
</div>
""",
    unsafe_allow_html=True,
)
