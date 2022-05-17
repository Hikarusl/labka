# Градиентная змейка с меняющимся фоном
## Описание игры
Игра представляет собой аналог классической змейки с некоторыми усовершенствованиями. Помимо роста змейки 
и увеличения ее скорости при съедании яблока, а также смерти в случае столкновения с хвостом или стенами,
в игре доступны:
* Смена цвета фона, на другой оттенок случайным образом, однако всегда выбирается светлый, чтобы у игрока не рябило в глазах;
* Онлайн табло подсчета очков, а также табло с рекордом по нескольким играм;
* Исчезающие правила, отображающиеся перед началом игры.
<p style="text-align: center;">
	<img src = './images/sample.png' alt='Скриншот игры' width="500" style="max-width: 70%;">
</p>  
<p style="text-align: center;">
	<img src = './images/sample2.png' alt='Скриншот игры2' width="500" style="max-width: 70%;">
</p>  


## Используемые технологии
* Игра написана с использованием классической игровой библиотеки pygame. 
* Для генерации фона, а также для перемещения яблока использована библиотека random.
* В проекте создана типичная файловая струтура, упрощающая дебаггинг и дальнейшее переиспользование блоков кода.


## Планы по доработке
В будущем планируется создать возможность выбора режима игры (уровень, запрет на столкновения со стенами или непрерывное движение).

---
_Проект разработан студентками МФТИ Гришиной Еленой, Забариной Светланой и Шабанской Ксенией, 2022_
