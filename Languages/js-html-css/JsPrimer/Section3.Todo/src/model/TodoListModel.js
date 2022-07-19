"use strict";

import { EventEmitter } from "../EventEmitter.js";
import { TodoItemModel } from "./TodoItemModel.js";

export class TodoListModel extends EventEmitter {
  #items;
  /**
   * @param {TodoItemModel[]} [items] 初期アイテム一覧（デフォルトは空の配列）
   */
  constructor(items = []) {
    super();
    this.#items = items;
  }

  /**
   * TodoItemの合計個数を返す
   * @returns {number}
   */
  getTotalCount() {
    return this.#items.length;
  }

  /**
   * 表示できるTodoItemの配列を返す
   * @returns {TodoItemModel[]}
   */
  getTodoItems() {
    return this.#items;
  }

  /**
   * TodoListの状態が更新されたときに呼び出されるリスナー関数を登録する
   * @param {Function} listener
   */
  onChange(listener) {
    this.addEventListener("change", listener);
  }

  offChange(listener) {
    this.removeEventListener("change", listener);
  }

  /**
   * 状態が変更されたときに呼ぶ。登録済みのリスナー関数を呼び出す
   */
  emitChange() {
    this.emit("change");
  }

  /**
   * TodoItemを追加する
   * @param {TodoItemModel} todoItem
   */
  addTodo(todoItem) {
    this.#items.push(todoItem);
    this.emitChange();
  }

  /**
   * Update completed Todoitem with id
   * @param {{id: number, completed: boolean}}
   */
  updateTodo({ id, completed }) {
    const todoItem = this.#items.find((todo) => todo.id === id);
    todoItem.completed = completed;
    this.emitChange();
  }

  /**
   * delete a id's TodoItem
   * @param {{id: number}}}
   */
  deleteTodo({ id }) {
    this.#items = this.#items.filter((todo) => {
      return todo.id !== id;
    });
    this.emitChange();
  }
}
