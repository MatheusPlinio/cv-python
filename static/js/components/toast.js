function setupToasts() {
    const toasts = document.querySelectorAll('.toast');
    
    toasts.forEach(toast => {
      setTimeout(() => {
        toast.classList.remove('opacity-0', 'translate-y-2');
      }, 10);
      const delay = toast.getAttribute('data-delay') || 5000;
      setTimeout(() => {
        toast.classList.add('opacity-0', 'translate-y-2');
        
        setTimeout(() => {
          toast.remove();
        }, 300);
      }, delay);
    });
  }
  
document.addEventListener('DOMContentLoaded', setupToasts);