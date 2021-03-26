Title: VUE学习笔记
Date: 2020-12-23 17:00
Category: Web
Tags: VUE
Authors: leelongcrazy
Summary: VUE学习笔记

# VUE学习笔记

## Vue 对象

##### new Vue()产生实例时传入的常用的选项

* el: 通过CSS选择器或者HTMLElement实例的方式，提供一个在页面上已存在的DOM元素作为Vue实例的挂在目标。
* data：用于定义属性
* methods：用于定义函数。Vue实例的事件，用于事件绑定
* template : 字符串模板，将会替换挂载的元素
* render : 字符串模板的代替方案
* props : 用于接收来自父组件的数据
* computed : 计算属性，用于简化模板的复杂数据计算
* watch : 观察Vue实例变化的一个表达式或计算属性函数
* directives : 自定义命令
* filters : 过滤器
* components : 组件

``` js
const vm = new Vue({
  // ...一些选项
});

vm.$data; // 获取 data
vm.$props; // 获取 props
vm.$el; // 获取挂载元素
vm.$options; // 获取 Vue 实例的初始选项
vm.$parent; // 获取父实例
vm.$root; // 获取根实例
vm.$children; // 获取当前实例的直接子组件
vm.$refs; // 获取持有注册过 ref 特性 的所有 DOM 元素和组件实例

vm.$watch; // 观察 Vue 实例变化的一个表达式或计算属性函数
vm.$set; // 向响应式对象中添加一个属性，并确保这个新属性同样是响应式的，且触发视图更新
vm.$delete; // 删除对象的属性。如果对象是响应式的，确保删除能触发更新视图
```





## 模板语法

### 插值

* 文本 {{ }}
* html: 使用v-html 指令用于输出HTML
* 属性：使用v-bind 指令用于绑定HTML属性中的值

### 表达式： 支持JS表达式

* 指令： 
  * v-if
  * v-on     它用于监听 DOM 事件
  * v-for
  * v-bind   属性值绑定

### 用户输入 ：v-model 指令来实现双向数据绑定

### 过滤器：

* {{ message | filterA | filterB }} // 
* {{ message | filterA('arg1', arg2) }}  过滤器是JavaScript函数，可以接受参数

### 缩写

* v-bind的缩写：

  * ``` html
    <!-- 完整语法 -->
    <a v-bind:href="url"></a>
    <!-- 缩写 -->
    <a :href="url"></a>
    ```

* v-on 的缩写：

  * ``` html
    <!-- 完整语法 -->
    <a v-on:click="doSomething"></a>
    <!-- 缩写 -->
    <a @click="doSomething"></a>
    ```



## 条件与循环

### 条件语句

* v-if
* v-else
* v-else-if
* v-show: 可以根据条件展示元素

### 循环语句

* v-for

  * 第一个参数为数据

  * 第二个参数为键名

  * 第三个参数为索引

  * ``` html
    <div id="app">
      <ul>
        <li v-for="(value, key, index) in object">
         {{ index }}. {{ key }} : {{ value }}
        </li>
      </ul>
    </div>
    ```



## 计算属性

计算属性关键词：computed，在处理一些复杂逻辑时是很有用的。

利用计算属性实现字符串的翻转：

``` html
<div id="app">
  <p>原始字符串: {{ message }}</p>
  <p>计算后反转字符串: {{ reversedMessage }}</p>
</div>
 
<script>
var vm = new Vue({
  el: '#app',
  data: {
    message: 'Runoob!'
  },
  computed: {
    // 计算属性的 getter
    reversedMessage: function () {
      // `this` 指向 vm 实例
      return this.message.split('').reverse().join('')
    }
  }
})
</script>
```

###### computed vs methods

可以用methods来替代computed，效果都是一样的，但是 computed 是基于它的依赖缓存，只有相关依赖发生改变时才会重新取值。而使用 methods ，在重新渲染的时候，函数总会重新调用执行。



## 监听属性

### watch

* 目的是响应数据的变化

* 深度监听：deep: true 

## 样式绑定

### class属性绑定

* ``` html 
  <div v-bind:class="{ 'active': isActive }"><div>
  ```

## 事件处理器

v-on

``` html
<!-- 同上 -->
<input v-on:keyup.enter="submit">
<!-- 缩写语法 -->
<input @keyup.enter="submit">
```



事件修饰符：

* `.stop` - 阻止冒泡
* `.prevent` - 阻止默认事件
* `.capture` - 阻止捕获
* `.self` - 只监听触发该元素的事件
* `.once` - 只触发一次
* `.left` - 左键事件
* `.right` - 右键事件
* `.middle` - 中间滚轮事件

监听键盘事件时添加按键修饰符，以下是按键别名：

* `.enter`
* `.tab`
* `.delete` (捕获 "删除" 和 "退格" 键)
* `.esc`
* `.space`
* `.up`
* `.down`
* `.left`
* `.right`
* `.ctrl`
* `.alt`
* `.shift`
* `.meta`



## 表单的处理

### v-model

修饰符：

* `.lazy`  输入框在change事件中变化
* `.number`  将输入值转换为Number类型
* `.trim`  自动过滤输入的首尾空格



## VUE 组件

组件（component）是VUE.js最强大的功能之一。

组件可以扩展HTML元素，封装可重用的代码。

注册全局组件语法格式：

``` html
Vue.component(tagName, options)
```

tagName为组件名，options为配置选项。

组件的调用：

``` html
<tagName> </tagName>
```

分类：全局组件和局部组件

### 自定义事件

组件中的 data 不是一个对象，而是一个函数，这样的好处就是每个实例可以维护一份被返回对象的独立的拷贝，如果 data 是一个对象则会影响到其他实例



### 自定义指令

``` js
<div id="app">
    <p>页面载入时，input 元素自动获取焦点：</p>
    <input v-focus>
</div>
 
<script>
// 注册一个全局自定义指令 v-focus
Vue.directive('focus', {
  // 当绑定元素插入到 DOM 中。
  inserted: function (el) {
    // 聚焦元素
    el.focus()
  }
})
// 创建根实例
new Vue({
  el: '#app'
})
</script>
```





## 消息传递

父组件可以使用 props 把数据传给子组件

子组件可以使用 $emit 触发父组件的自定义事件

``` js
vm.$emit( event, arg ) //触发当前实例上的事件

vm.$on( event, fn );//监听event事件后运行 fn
```

## VUE 的过渡和动画

实现过渡效果的组件：transition

## Vue.js Ajax(axios)

Vue.js 2.0 版本推荐使用 axios 来完成 ajax 请求。

Axios 是一个基于 Promise 的 HTTP 库，可以用在浏览器和 node.js 中。

Github开源地址： https://github.com/axios/axios

使用：

``` html
<script src="https://cdn.staticfile.org/axios/0.18.0/axios.min.js"></script>
```

