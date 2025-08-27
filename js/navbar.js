function initNavbar() {
    // 导航栏滚动效果
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('py-2', 'bg-opacity-95', 'shadow-md');
                navbar.classList.remove('py-4', 'bg-opacity-90');
            } else {
                navbar.classList.add('py-4', 'bg-opacity-90');
                navbar.classList.remove('py-2', 'bg-opacity-95', 'shadow-md');
            }
        });
    }

    // 移动端菜单切换
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
            // 切换图标
            const icon = menuToggle.querySelector('i');
            if (icon.classList.contains('fa-bars')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // 移动端子菜单切换
    const submenuToggles = document.querySelectorAll('.mobile-submenu-toggle');
    submenuToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            e.preventDefault();
            const submenu = toggle.closest('div').nextElementSibling;
            if (submenu) {
                submenu.classList.toggle('hidden');
                // 切换图标方向
                if (toggle.style.transform === 'rotate(180deg)') {
                    toggle.style.transform = 'rotate(0)';
                } else {
                    toggle.style.transform = 'rotate(180deg)';
                }
            }
        });
    });
}

// 页面加载完成后初始化导航栏
document.addEventListener('DOMContentLoaded', initNavbar);