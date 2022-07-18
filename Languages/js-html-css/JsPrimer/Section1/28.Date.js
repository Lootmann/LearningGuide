/*
 *
 */
"use strict";

import { title, subtitle, l } from "./util.js";

title("Date");
{
  const now = new Date();

  l(Date.now());
  l(now.getTime());
  l(now.toISOString());
}

title("Date FullYear, Month, Day");
{
  function formatDate(date) {
    const yyyy = String(date.getFullYear());
    const mm = String(date.getMonth() + 1).padStart(2, "0");
    const dd = String(date.getDate()).padStart(2, "0");
    return `${yyyy}/${mm}/${dd}`;
  }

  const date = new Date("2008-02-04T15:04:05.999");
  l(formatDate(date));
}
