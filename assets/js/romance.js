// ===== 二次元浪漫氛围动画 =====
// 生成飘落樱花瓣、闪烁星星、流星、漂浮爱心

(function () {
  'use strict';
  // 尊重系统减少动态效果偏好
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // 快速随机工具
  function rand(min, max) { return min + Math.random() * (max - min); }
  function intRand(min, max) { return Math.floor(rand(min, max + 1)); }

  // 背景容器
  var bg = document.createElement('div');
  bg.className = 'sakura-bg';
  document.body.prepend(bg);

  // ---- 闪烁星星 ----
  function makeStars() {
    var count = window.innerWidth < 768 ? 40 : 70;
    for (var i = 0; i < count; i++) {
      var s = document.createElement('div');
      s.className = 'twinkle-star';
      s.style.left = rand(0, 100) + '%';
      s.style.top = rand(0, 100) + '%';
      s.style.setProperty('--dur', rand(2, 6).toFixed(2) + 's');
      s.style.setProperty('--delay', rand(0, 6).toFixed(2) + 's');
      var size = rand(1.5, 4);
      s.style.width = size + 'px';
      s.style.height = size + 'px';
      bg.appendChild(s);
    }
  }

  // ---- 流星 ----
  function makeShootingStars() {
    for (var i = 0; i < 3; i++) {
      var m = document.createElement('div');
      m.className = 'shooting-star';
      m.style.top = rand(0, 40) + '%';
      m.style.left = rand(60, 110) + '%';
      m.style.setProperty('--dur', rand(7, 12).toFixed(1) + 's');
      m.style.setProperty('--delay', rand(2, 12).toFixed(1) + 's');
      bg.appendChild(m);
    }
  }

  // ---- 飘落樱花瓣 ----
  function makePetals() {
    var count = window.innerWidth < 768 ? 12 : 20;
    for (var i = 0; i < count; i++) {
      var p = document.createElement('div');
      p.className = 'sakura-petal';
      var size = rand(10, 20);
      p.style.left = rand(0, 100) + '%';
      p.style.setProperty('--size', size.toFixed(1) + 'px');
      p.style.setProperty('--dur', rand(8, 16).toFixed(1) + 's');
      p.style.setProperty('--delay', rand(0, 12).toFixed(1) + 's');
      p.style.setProperty('--sway', rand(20, 80).toFixed(0) + 'px');
      p.style.opacity = rand(0.4, 0.9);
      bg.appendChild(p);
    }
  }

  // ---- 漂浮爱心 ----
  var HEARTS = ['💗', '💕', '✨', '🌷', '💞', 'in', '🌸'];
  function makeHearts() {
    var count = window.innerWidth < 768 ? 6 : 10;
    for (var i = 0; i < count; i++) {
      var h = document.createElement('div');
      h.className = 'heart-float';
      h.textContent = '💗';
      h.style.left = rand(2, 98) + '%';
      h.style.fontSize = intRand(12, 24) + 'px';
      h.style.setProperty('--dur', rand(5, 9).toFixed(1) + 's');
      h.style.setProperty('--delay', rand(0, 8).toFixed(1) + 's');
      document.body.appendChild(h);
    }
  }

  makeStars();
  makeShootingStars();
  makePetals();
  makeHearts();
})();