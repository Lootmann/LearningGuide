"use strict";

// Data needed for a later exercise
const flights =
  "_Delayed_Departure;fao93766109;txl2133758440;11:25+_Arrival;bru0943384722;fao93766109;11:45+_Delayed_Arrival;hel7439299980;fao93766109;12:05+_Departure;fao93766109;lis2323639855;12:30";

// Data needed for first part of the section
const restaurant = {
  name: "Classico Italiano",
  location: "Via Angelo Tavanti 23, Firenze, Italy",
  categories: ["Italian", "Pizzeria", "Vegetarian", "Organic"],
  starterMenu: ["Focaccia", "Bruschetta", "Garlic Bread", "Caprese Salad"],
  mainMenu: ["Pizza", "Pasta", "Risotto"],

  openingHours: {
    thu: {
      open: 12,
      close: 22,
    },
    fri: {
      open: 11,
      close: 23,
    },
    sat: {
      open: 0, // Open 24 hours
      close: 24,
    },
  },

  // functions
  order: function (startIndex, mainIndex) {
    return [this.starterMenu[startIndex], this.mainMenu[mainIndex]];
  },

  // obj args
  orderDelivery: function ({
    starterIndex = 1,
    mainIndex = 1,
    time = "20:00",
    address,
  }) {
    return `Order received! ${this.starterMenu[starterIndex]} and ${this.mainMenu[mainIndex]} will be delivered to ${address} at ${time}`;
  },
};

//
//
//
function title(msg) {
  console.log(`\n>>> ${msg}`);
}

function print(...elems) {
  console.log(elems);
}

const p = print;

title("destructuring");
{
  const [first, second] = restaurant["categories"];
  print(first, second);
}
{
  const [first, second] = restaurant.categories;
  print(first, second);

  const [f, , s] = restaurant.categories;
  print(f, s);
}

title("swap with array destructuring");
{
  let [main, , secondary] = restaurant.categories;
  print(main, secondary);

  [main, secondary] = [secondary, main];
  print(main, secondary);
}

{
  const [starter, mainCourse] = restaurant.order(2, 0);
  print(starter, mainCourse);
}

title("nested array");
{
  const nested = [2, 4, [5, 6]];
  const [x, , z] = nested;
  print(x, z);

  const [i, , [j, k]] = nested;
  print(i, j, k); // 2, [5, 6]
}

title("Default values");
{
  const [p, q, r] = [8, 9];
  print(p, q, r);
}

title("Object Destructuring");
{
  const { name, openingHours, categories } = restaurant;
  p(name, openingHours, categories);
}

title("Named Object Destructuring");
{
  const {
    name: restaurantName,
    openingHours: hours,
    categories: tags,
  } = restaurant;

  p(restaurantName, hours, tags);
}

title("Default Values");
{
  const { menu = [], starterMenu: starters = [] } = restaurant;
  p(menu, starters);

  const {
    fri: { open: o, close: c },
  } = restaurant.openingHours;
  p(o, c);
}

title("Object Destructuring");
{
  const o = restaurant.orderDelivery({
    time: "22:30",
    address: "Via del Sole, 21",
    mainIndex: 2,
    starterIndex: 2,
  });
  p(o);

  const q = restaurant.orderDelivery({
    address: "Via del Sole, 21",
    starterIndex: 1,
  });
  p(q);
}
