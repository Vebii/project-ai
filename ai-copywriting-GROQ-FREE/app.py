from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

# Konfigurasi API Key (ganti dengan API key Anda dari Groq)
GROQ_API_KEY = os.environ.get('GROQ_API_KEY', 'your-groq-api-key-here')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Check API key
        if not GROQ_API_KEY or GROQ_API_KEY == 'your-groq-api-key-here':
            return jsonify({
                'success': False,
                'error': 'API key belum diatur. Silakan set GROQ_API_KEY di file .env atau environment variable. Dapatkan gratis di: https://console.groq.com/'
            }), 400
        
        data = request.json
        content_type = data.get('content_type')
        topic = data.get('topic')
        tone = data.get('tone', 'professional')
        language = data.get('language', 'indonesian')
        
        # Buat prompt berdasarkan jenis konten
        prompt = create_prompt(content_type, topic, tone, language)
        
        # Panggil Groq API (GRATIS & CEPAT!)
        headers = {
            'Authorization': f'Bearer {GROQ_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
           'model': 'llama-3.3-70b-versatile',  # Model gratis terbaik dari Groq
            'messages': [
                {
                    'role': 'system',
                    'content': 'You are an expert copywriter and marketing content creator. Create compelling, persuasive, and engaging copy that converts.'
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'temperature': 0.7,
            'max_tokens': 1024,
            'top_p': 1
        }
        
        response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result_data = response.json()
            result_text = result_data['choices'][0]['message']['content']
            
            return jsonify({
                'success': True,
                'result': result_text
            })
        elif response.status_code == 401:
            return jsonify({
                'success': False,
                'error': 'API key tidak valid. Periksa kembali API key Anda di console.groq.com/keys'
            }), 401
        elif response.status_code == 429:
            return jsonify({
                'success': False,
                'error': 'Rate limit tercapai. Tunggu sebentar dan coba lagi. (Groq: 30 req/menit gratis)'
            }), 429
        else:
            error_msg = response.json().get('error', {}).get('message', 'Unknown error')
            return jsonify({
                'success': False,
                'error': f'API Error: {error_msg}'
            }), response.status_code
        
    except requests.exceptions.Timeout:
        return jsonify({
            'success': False,
            'error': 'Request timeout. Coba lagi dalam beberapa saat.'
        }), 408
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': f'Network error: {str(e)}'
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Terjadi kesalahan: {str(e)}'
        }), 500

def create_prompt(content_type, topic, tone, language):
    """Membuat prompt berdasarkan jenis konten"""
    
    lang_instruction = f"Write in Indonesian (Bahasa Indonesia)." if language == 'indonesian' else "Write in English."
    
    prompts = {
        'ad_copy': f"""
        {lang_instruction}
        Create compelling advertising copy about: {topic}
        
        Tone: {tone}
        
        Provide:
        1. A powerful headline
        2. Engaging body copy
        3. Strong call-to-action
        
        Make it ready to use and persuasive.
        """,
        
        'slogan': f"""
        {lang_instruction}
        Create 5 catchy and memorable slogans for: {topic}
        
        Tone: {tone}
        
        Each slogan should be:
        - Short (maximum 8 words)
        - Memorable
        - Reflect brand values
        
        Number each slogan (1-5).
        """,
        
        'product_description': f"""
        {lang_instruction}
        Create an attractive product description for: {topic}
        
        Tone: {tone}
        
        Include:
        1. Attention-grabbing headline
        2. Key benefits description
        3. Call-to-action
        
        Make it compelling and conversion-focused.
        """,
        
        'social_media': f"""
        {lang_instruction}
        Create 3 social media posts about: {topic}
        
        Tone: {tone}
        
        For each post provide:
        - Engaging caption
        - Relevant hashtags
        - Call-to-action
        
        Label each as Post 1, Post 2, Post 3.
        """,
        
        'email_marketing': f"""
        {lang_instruction}
        Create an email marketing campaign about: {topic}
        
        Tone: {tone}
        
        Include:
        1. Compelling subject line
        2. Personal opening
        3. Persuasive body
        4. Clear call-to-action
        
        Format it as a complete email.
        """,
        
        'blog_intro': f"""
        {lang_instruction}
        Create an engaging blog post introduction about: {topic}
        
        Tone: {tone}
        
        The intro should:
        - Hook readers in the first paragraph
        - Explain the problem/topic
        - Preview what will be discussed
        
        Make it 2-3 paragraphs long.
        """
    }
    
    return prompts.get(content_type, prompts['ad_copy'])

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 AI COPYWRITING PRO - GROQ EDITION (100% GRATIS!)")
    print("=" * 60)
    print("📌 Dapatkan API key gratis di: https://console.groq.com/")
    print("💡 Model: Llama 3.1 70B (Sangat cepat & gratis unlimited!)")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
