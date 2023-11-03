from transformers import pipeline
classifier = pipeline ("sentiment-analysis,
                       blanchefort/rubert-base-cased-sentiment"
classifier("У меня репозиторий не клонируется в виртуальный линукс. 
Пишет Не удалось прочитать из внешнего репозитория. Удостоверьтесь, 
что у вас есть необходимые права доступа и репозиторий существует")
