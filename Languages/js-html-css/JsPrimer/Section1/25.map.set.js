/*
 * Map, Set
 */
"use strict";

import { title, subtitle, l } from "./util.js";

// Map ...
// マップ型のコレクション, dict, hashmap, 連想配列
title("Map");
{
  const map = new Map();
  l(map.size);
}

// "key", "value"
title("Map with initializations");
{
  const map = new Map([
    ["key1", "value1"],
    ["key2", "value2"],
  ]);

  l(map);
  l(map.size);
}

title("set, get, has");
{
  const map = new Map();
  map.set("k1", "v1");
  l(map);
  l(map.size);
  l(map.get("k1"));

  for (let i = 2; i <= 4; i++) {
    map.set(`k${i}`, `k${i}`);
  }

  l(map);
  l(map.size);
  l(map.has("k1"));
  l(map.has("v2"));
  l(map.has("k3"));
}

title("map forloops");
{
  const map = new Map();

  for (let i = 0; i <= 4; i++) {
    map.set(`k${i}`, `k${i}`);
  }

  l(map);

  subtitle(".forEach");
  const res1 = [];
  map.forEach((v, k) => {
    res1.push(`(${v}, ${k})`);
  });
  l(res1);

  subtitle(".keys");
  l(map.keys());

  subtitle(".entries");
  l(map.entries());

  subtitle("for ... of");
  const res2 = [];
  for (const [k, v] of map) res2.push(`(${v}, ${k}`);
  l(res2);
}

title("Shopping Cart with map");
{
  class ShoppingCart {
    constructor() {
      this.items = new Map();
    }

    addItem(item) {
      const count = this.items.get(item) ?? 0;
      this.items.set(item, count + 1);
    }

    getTotalPrice() {
      return Array.from(this.items).reduce((total, [item, count]) => {
        return total + item.price * count;
      }, 0);
    }

    toString() {
      return Array.from(this.items)
        .map(([item, count]) => {
          return `${item.name}:${count}`;
        })
        .join(",");
    }
  }

  const shoppingCart = new ShoppingCart();
  const shopItems = [
    { name: "みかん", price: 100 },
    { name: "リンゴ", price: 200 },
  ];
  shoppingCart.addItem(shopItems[0]);
  shoppingCart.addItem(shopItems[0]);
  shoppingCart.addItem(shopItems[1]);

  console.log(shoppingCart.getTotalPrice()); // => 400
  console.log(shoppingCart.toString()); // => "みかん:2,リンゴ:1"
}
