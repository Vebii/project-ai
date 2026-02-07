document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('copywritingForm');
    const generateBtn = document.getElementById('generateBtn');
    const btnText = document.querySelector('.btn-text');
    const btnLoader = document.querySelector('.btn-loader');
    const resultSection = document.getElementById('resultSection');
    const resultBox = document.getElementById('result');
    const copyBtn = document.getElementById('copyBtn');

    // Handle form submission
    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Get form data
        const formData = {
            content_type: document.getElementById('contentType').value,
            topic: document.getElementById('topic').value,
            tone: document.getElementById('tone').value,
            language: document.getElementById('language').value
        };

        // Validate
        if (!formData.content_type || !formData.topic) {
            showToast('Mohon lengkapi semua field yang diperlukan', 'error');
            return;
        }

        // Show loading state
        generateBtn.disabled = true;
        btnText.style.display = 'none';
        btnLoader.style.display = 'inline-block';
        resultSection.style.display = 'none';

        try {
            // Call API
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();

            if (data.success) {
                // Show result
                resultBox.textContent = data.result;
                resultSection.style.display = 'block';
                
                // Smooth scroll to result
                resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                
                showToast('Copywriting berhasil di-generate! ✨', 'success');
            } else {
                showToast('Error: ' + data.error, 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            showToast('Terjadi kesalahan. Pastikan API key sudah diatur dengan benar.', 'error');
        } finally {
            // Reset button state
            generateBtn.disabled = false;
            btnText.style.display = 'inline-block';
            btnLoader.style.display = 'none';
        }
    });

    // Handle copy button
    copyBtn.addEventListener('click', function() {
        const text = resultBox.textContent;
        
        // Copy to clipboard
        navigator.clipboard.writeText(text).then(function() {
            // Change button text temporarily
            const originalText = copyBtn.textContent;
            copyBtn.textContent = '✅ Copied!';
            
            showToast('Copywriting berhasil di-copy! 📋', 'success');
            
            setTimeout(function() {
                copyBtn.textContent = originalText;
            }, 2000);
        }).catch(function(err) {
            console.error('Error copying text: ', err);
            showToast('Gagal copy. Silakan copy manual.', 'error');
        });
    });

    // Toast notification function
    function showToast(message, type = 'success') {
        // Remove existing toast
        const existingToast = document.querySelector('.toast');
        if (existingToast) {
            existingToast.remove();
        }

        // Create toast
        const toast = document.createElement('div');
        toast.className = 'toast';
        toast.textContent = message;
        
        if (type === 'error') {
            toast.style.background = '#ef4444';
        }

        document.body.appendChild(toast);

        // Remove after 3 seconds
        setTimeout(function() {
            toast.style.animation = 'slideOut 0.3s ease-out';
            setTimeout(function() {
                toast.remove();
            }, 300);
        }, 3000);
    }

    // Add slideOut animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideOut {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(400px);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
});
