from django.shortcuts import render
from django.http import JsonResponse
from transformers import T5Tokenizer, T5ForConditionalGeneration

def call_chatbot(request):
    return render(request, "chatbot.html")

model_name = "KhantKyaw/T5-small_new_chatbot"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def chat_response(request):
    user_message = request.GET.get('message', '')
    print(user_message)

    if user_message:
        input_ids = tokenizer.encode(user_message, return_tensors='pt')
        outputs = model.generate(input_ids,
                                min_length=5,
                                max_length=300,
                                do_sample=True, num_beams=5, no_repeat_ngram_size=2)
        

        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return JsonResponse({'response': generated_text})
    else:
        return JsonResponse({'response': 'Please enter a message.'})



