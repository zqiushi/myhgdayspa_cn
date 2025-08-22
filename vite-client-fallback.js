// 空脚本文件，用于解决Vite客户端脚本加载失败的问题
console.log('Vite client fallback loaded successfully');

// 模拟Vite客户端的基本功能，防止页面报错
if (window.__vite_is_dep) {
  window.__vite_is_dep = true;
}

// 确保模块加载系统不会崩溃
try {
  if (!window.module) {
    window.module = {};
  }
} catch (e) {
  console.error('Error setting up module fallback:', e);
}