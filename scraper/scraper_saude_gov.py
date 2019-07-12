from bs4 import BeautifulSoup

from urllib.request import urlopen

import requests

import csv

import pandas as pd

import os

#link = urlopen("https://brasil.elpais.com/seccion/tecnologia")

#soup = BeautifulSoup(link, "html.parser")

headers = {'User-Agent': 'Py_Scraper'}

#link = "https://brasil.elpais.com/seccion/politica" 

lista_titulo = []
lista_corpo = []
lista_url = []

var = True
pagina = 100

lista = []

print('Inicializando...')

html_doc = """
<form action="http://www.saude.gov.br/fakenews" method="post" name="adminForm" id="adminForm" class="form-inline">
        <div class="row-fluid row-busca">
        <fieldset class="filters alert alert-info">
            <legend class="hide">Filtros</legend>

            <div class="row-fluid row-busca-f">
                <input type="text" name="filter-search" id="filter-search" class="span4 input-busca" onchange="document.adminForm.submit();" value="FAKE NEWS" title="Filtrar Conteúdo da Pesquisa" placeholder="Filtro por Título">
                <button type="submit" class="acao-busca button btn btn-primary">Buscar</button>
                <button type="button" class="acao-busca button btn btn-warning" onclick="limparFiltros();">
                    Limpar              </button>

                                <select id="limit" name="limit" class="inputbox input-mini" size="1" onchange="this.form.submit()">
    <option value="5">5</option>
    <option value="10">10</option>
    <option value="15">15</option>
    <option value="20">20</option>
    <option value="25">25</option>
    <option value="30">30</option>
    <option value="50">50</option>
    <option value="100">100</option>
    <option value="0" selected="selected">Todos</option>
</select>
                    </div>

        <div class="row-fluid row-busca-f datasRange span5">
            <div class="control-group info span6">
                <label class="control-label" for="inputInfo">Data Inicio:</label>
                <div class="controls">
                    <div class="field-calendar">
        <div class="input-append">
                <input type="text" id="filter-start_date" name="filter-start_date" data-alt-value="" autocomplete="off">
        <button type="button" class="btn btn-secondary" id="filter-start_date_btn" data-inputfield="filter-start_date" data-dayformat="%Y-%m-%d" data-button="filter-start_date_btn" data-firstday="0" data-weekend="0,6" data-today-btn="1" data-week-numbers="1" data-show-time="0" data-show-others="1" data-time-24="24" data-only-months-nav="0" title="Abrir o calendário"><span class="icon-calendar" aria-hidden="true"></span></button>
            </div>
<div style="direction: ltr; position: absolute; box-shadow: rgba(0, 0, 0, 0.67) 0px 0px 70px 0px; min-width: 0px; padding: 0px; display: none; left: auto; top: auto; z-index: 1060; border-radius: 20px;" class="js-calendar"><div class="calendar-container"><table class="table" style="margin-bottom: 0px; visibility: visible;" cellspacing="0" cellpadding="0"><thead class="calendar-header"><tr class="calendar-head-row"><td colspan="1" style="text-align: center; font-size: 18px; line-height: 18px;" class=" nav"><a class="js-btn btn-prev-year" style="display:inline;padding:2px 6px;cursor:pointer;text-decoration:none;" unselectable="on">‹</a></td><td colspan="6" class="title"><div unselectable="on"><div style="text-align:center;font-size:18px"><span>2019</span></div></div></td><td colspan="1" style="text-align: center; font-size: 18px; line-height: 18px;" class=" nav"><a class="js-btn btn-next-year" style="display:inline;padding:2px 6px;cursor:pointer;text-decoration:none;" unselectable="on"> ›</a></td></tr><tr class="calendar-head-row"><td colspan="1" style="text-align: center; font-size: 2em; line-height: 1em;" class=" nav"><a class="js-btn btn-prev-month" style="display:inline;padding:2px 6px;cursor:pointer;text-decoration:none;" unselectable="on">‹</a></td><td colspan="6" style="text-align: center;" class="title"><div unselectable="on"><div style="text-align:center;font-size:1.2em"><span>Julho</span></div></div></td><td colspan="1" style="text-align: center; font-size: 2em; line-height: 1em;" class=" nav"><a class="js-btn btn-next-month" style="display:inline;padding:2px 6px;cursor:pointer;text-decoration:none;" unselectable="on"> ›</a></td></tr><tr class="daynames wk"><td class="day-name wn">sem</td><td class="day-name day-name-week">Dom</td><td class="day-name day-name-week">Seg</td><td class="day-name day-name-week">Ter</td><td class="day-name day-name-week">Qua</td><td class="day-name day-name-week">Qui</td><td class="day-name day-name-week">Sex</td><td class="day-name day-name-week">Sab</td></tr></thead><tbody><tr class="daysrow wk"><td class="day wn">26</td><td class="day disabled othermonth  weekend" style="text-align: center;">30</td><td class="day" style="text-align: center; cursor: pointer;">1</td><td class="day" style="text-align: center; cursor: pointer;">2</td><td class="day" style="text-align: center; cursor: pointer;">3</td><td class="day" style="text-align: center; cursor: pointer;">4</td><td class="day" style="text-align: center; cursor: pointer;">5</td><td class="day weekend" style="text-align: center; cursor: pointer;">6</td></tr><tr class="daysrow wk"><td class="day wn">27</td><td class="day weekend" style="text-align: center; cursor: pointer;">7</td><td class="day" style="text-align: center; cursor: pointer;">8</td><td class="day" style="text-align: center; cursor: pointer;">9</td><td class="day selected today" style="text-align: center; cursor: pointer;">10</td><td class="day" style="text-align: center; cursor: pointer;">11</td><td class="day" style="text-align: center; cursor: pointer;">12</td><td class="day weekend" style="text-align: center; cursor: pointer;">13</td></tr><tr class="daysrow wk"><td class="day wn">28</td><td class="day weekend" style="text-align: center; cursor: pointer;">14</td><td class="day" style="text-align: center; cursor: pointer;">15</td><td class="day" style="text-align: center; cursor: pointer;">16</td><td class="day" style="text-align: center; cursor: pointer;">17</td><td class="day" style="text-align: center; cursor: pointer;">18</td><td class="day" style="text-align: center; cursor: pointer;">19</td><td class="day weekend" style="text-align: center; cursor: pointer;">20</td></tr><tr class="daysrow wk"><td class="day wn">29</td><td class="day weekend" style="text-align: center; cursor: pointer;">21</td><td class="day" style="text-align: center; cursor: pointer;">22</td><td class="day" style="text-align: center; cursor: pointer;">23</td><td class="day" style="text-align: center; cursor: pointer;">24</td><td class="day" style="text-align: center; cursor: pointer;">25</td><td class="day" style="text-align: center; cursor: pointer;">26</td><td class="day weekend" style="text-align: center; cursor: pointer;">27</td></tr><tr class="daysrow wk"><td class="day wn">30</td><td class="day weekend" style="text-align: center; cursor: pointer;">28</td><td class="day" style="text-align: center; cursor: pointer;">29</td><td class="day" style="text-align: center; cursor: pointer;">30</td><td class="day" style="text-align: center; cursor: pointer;">31</td><td class="day disabled othermonth " style="text-align: center;">1</td><td class="day disabled othermonth " style="text-align: center;">2</td><td class="day disabled othermonth  weekend" style="text-align: center;">3</td></tr><tr class="daysrow wk"><td class="day wn">31</td><td class="day disabled othermonth  weekend" style="text-align: center;">4</td><td class="day disabled othermonth " style="text-align: center;">5</td><td class="day disabled othermonth " style="text-align: center;">6</td><td class="day disabled othermonth " style="text-align: center;">7</td><td class="day disabled othermonth " style="text-align: center;">8</td><td class="day disabled othermonth " style="text-align: center;">9</td><td class="day disabled othermonth  weekend" style="text-align: center;">10</td></tr></tbody></table><div class="buttons-wrapper btn-group"><button type="button" data-action="clear" class="js-btn btn btn-clear">Limpar</button><button type="button" data-action="today" class="js-btn btn btn-today">Hoje</button><button type="button" data-action="exit" class="js-btn btn btn-exit">Fechar</button></div></div></div></div>
                </div>
            </div>
            <div class="control-group info span6">
                <label class="control-label" for="inputInfo">Data Fim:</label>
                <div class="controls">
                    <div class="field-calendar">
        <div class="input-append">
                <input type="text" id="filter-end_date" name="filter-end_date" data-alt-value="" autocomplete="off">
        <button type="button" class="btn btn-secondary" id="filter-end_date_btn" data-inputfield="filter-end_date" data-dayformat="%Y-%m-%d 23:59:59" data-button="filter-end_date_btn" data-firstday="0" data-weekend="0,6" data-today-btn="1" data-week-numbers="1" data-show-time="0" data-show-others="1" data-time-24="24" data-only-months-nav="0" title="Abrir o calendário"><span class="icon-calendar" aria-hidden="true"></span></button>
            </div>
<div style="direction: ltr; position: absolute; box-shadow: rgba(0, 0, 0, 0.67) 0px 0px 70px 0px; min-width: 0px; padding: 0px; display: none; left: auto; top: auto; z-index: 1060; border-radius: 20px;" class="js-calendar"><div class="calendar-container"><table class="table" style="margin-bottom: 0px; visibility: visible;" cellspacing="0" cellpadding="0"><thead class="calendar-header"><tr class="calendar-head-row"><td colspan="1" style="text-align: center; font-size: 18px; line-height: 18px;" class=" nav"><a class="js-btn btn-prev-year" style="display:inline;padding:2px 6px;cursor:pointer;text-decoration:none;" unselectable="on">‹</a></td><td colspan="6" class="title"><div unselectable="on"><div style="text-align:center;font-size:18px"><span>2019</span></div></div></td><td colspan="1" style="text-align: center; font-size: 18px; line-height: 18px;" class=" nav"><a class="js-btn btn-next-year" style="display:inline;padding:2px 6px;cursor:pointer;text-decoration:none;" unselectable="on"> ›</a></td></tr><tr class="calendar-head-row"><td colspan="1" style="text-align: center; font-size: 2em; line-height: 1em;" class=" nav"><a class="js-btn btn-prev-month" style="display:inline;padding:2px 6px;cursor:pointer;text-decoration:none;" unselectable="on">‹</a></td><td colspan="6" style="text-align: center;" class="title"><div unselectable="on"><div style="text-align:center;font-size:1.2em"><span>Julho</span></div></div></td><td colspan="1" style="text-align: center; font-size: 2em; line-height: 1em;" class=" nav"><a class="js-btn btn-next-month" style="display:inline;padding:2px 6px;cursor:pointer;text-decoration:none;" unselectable="on"> ›</a></td></tr><tr class="daynames wk"><td class="day-name wn">sem</td><td class="day-name day-name-week">Dom</td><td class="day-name day-name-week">Seg</td><td class="day-name day-name-week">Ter</td><td class="day-name day-name-week">Qua</td><td class="day-name day-name-week">Qui</td><td class="day-name day-name-week">Sex</td><td class="day-name day-name-week">Sab</td></tr></thead><tbody><tr class="daysrow wk"><td class="day wn">26</td><td class="day disabled othermonth  weekend" style="text-align: center;">30</td><td class="day" style="text-align: center; cursor: pointer;">1</td><td class="day" style="text-align: center; cursor: pointer;">2</td><td class="day" style="text-align: center; cursor: pointer;">3</td><td class="day" style="text-align: center; cursor: pointer;">4</td><td class="day" style="text-align: center; cursor: pointer;">5</td><td class="day weekend" style="text-align: center; cursor: pointer;">6</td></tr><tr class="daysrow wk"><td class="day wn">27</td><td class="day weekend" style="text-align: center; cursor: pointer;">7</td><td class="day" style="text-align: center; cursor: pointer;">8</td><td class="day" style="text-align: center; cursor: pointer;">9</td><td class="day selected today" style="text-align: center; cursor: pointer;">10</td><td class="day" style="text-align: center; cursor: pointer;">11</td><td class="day" style="text-align: center; cursor: pointer;">12</td><td class="day weekend" style="text-align: center; cursor: pointer;">13</td></tr><tr class="daysrow wk"><td class="day wn">28</td><td class="day weekend" style="text-align: center; cursor: pointer;">14</td><td class="day" style="text-align: center; cursor: pointer;">15</td><td class="day" style="text-align: center; cursor: pointer;">16</td><td class="day" style="text-align: center; cursor: pointer;">17</td><td class="day" style="text-align: center; cursor: pointer;">18</td><td class="day" style="text-align: center; cursor: pointer;">19</td><td class="day weekend" style="text-align: center; cursor: pointer;">20</td></tr><tr class="daysrow wk"><td class="day wn">29</td><td class="day weekend" style="text-align: center; cursor: pointer;">21</td><td class="day" style="text-align: center; cursor: pointer;">22</td><td class="day" style="text-align: center; cursor: pointer;">23</td><td class="day" style="text-align: center; cursor: pointer;">24</td><td class="day" style="text-align: center; cursor: pointer;">25</td><td class="day" style="text-align: center; cursor: pointer;">26</td><td class="day weekend" style="text-align: center; cursor: pointer;">27</td></tr><tr class="daysrow wk"><td class="day wn">30</td><td class="day weekend" style="text-align: center; cursor: pointer;">28</td><td class="day" style="text-align: center; cursor: pointer;">29</td><td class="day" style="text-align: center; cursor: pointer;">30</td><td class="day" style="text-align: center; cursor: pointer;">31</td><td class="day disabled othermonth " style="text-align: center;">1</td><td class="day disabled othermonth " style="text-align: center;">2</td><td class="day disabled othermonth  weekend" style="text-align: center;">3</td></tr><tr class="daysrow wk"><td class="day wn">31</td><td class="day disabled othermonth  weekend" style="text-align: center;">4</td><td class="day disabled othermonth " style="text-align: center;">5</td><td class="day disabled othermonth " style="text-align: center;">6</td><td class="day disabled othermonth " style="text-align: center;">7</td><td class="day disabled othermonth " style="text-align: center;">8</td><td class="day disabled othermonth " style="text-align: center;">9</td><td class="day disabled othermonth  weekend" style="text-align: center;">10</td></tr></tbody></table><div class="buttons-wrapper btn-group"><button type="button" data-action="clear" class="js-btn btn btn-clear">Limpar</button><button type="button" data-action="today" class="js-btn btn btn-today">Hoje</button><button type="button" data-action="exit" class="js-btn btn btn-exit">Fechar</button></div></div></div></div>
                </div>
            </div>
        </div>

        <input type="hidden" name="filter_order" value="">
        <input type="hidden" name="filter_order_Dir" value="">
        <input type="hidden" name="limitstart" value="">
        <input type="hidden" name="task" value="">
    </fieldset>
</div>



    <div class="tile-list-1">
        
        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45583-fraldas-geriatricas-para-adulto-gratis-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/C--pia-de-C--pia-de-C--pia-de-C--pia-de-C--pia-de-C--pia.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45583-fraldas-geriatricas-para-adulto-gratis-e-fake-news">Fraldas geriátricas para adulto grátis - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Fraldas geriátricas para adulto grátis - É FAKE NEWS!               <p>Olá. A 
disponibilização de fraldas geriátricas pelo Farmácia Popular é 
verídica. No entanto, *elas não são gratuitas, mas, sim, dispensadas com
 até 90% de desconto*.
Você...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 10/07/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 11h55</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45563-doacao-de-sangue-ab-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Fake-news-sangue-ab.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45563-doacao-de-sangue-ab-e-fake-news">Doação de sangue AB - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Doação de sangue AB - É FAKE NEWS!              <p>Olá, por mais que a intenção possa ter sido boa, essa mensagem é falsa! Não compartilhe.
A mensagem tem caráter alarmista, não há detalhes importantes como endereço, nomes e...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 02/07/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 14h33</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45548-cloro-previne-a-dengue-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/dengue-cloro-fakenews.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45548-cloro-previne-a-dengue-e-fake-news">Cloro previne a dengue - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Cloro previne a dengue - É FAKE NEWS!               <p>Olá, essa notícia é 
falsa! Não compartilhe! O texto contém características de Fake News, 
como erro de gramática, alarmista, informações vagas, não há datas e 
fontes confiáveis...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 24/06/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 18h55</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45547-recurso-para-cirurgias-eletivas-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/fake-news-eletivas.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45547-recurso-para-cirurgias-eletivas-e-fake-news">Recurso para cirurgias eletivas - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Recurso para cirurgias eletivas - É FAKE NEWS!              <p>Olá! Não 
compartilhe essa mensagem, ela é falsa. Além de ter todas as 
características de Fake News, como tom alarmistas, erros de português e 
imprecisão em informações - não há...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 24/06/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 18h47</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45545-cura-do-cancer-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/fake-news-gupta.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45545-cura-do-cancer-e-fake-news">Cura do câncer - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Cura do câncer - É FAKE NEWS!               <p>Olá, essa notícia é falsa! Não 
compartilhe! O texto contém características de Fake News, como erro de 
gramática, alarmista, informações vagas, não há datas e fontes 
confiáveis...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 24/06/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 18h26</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45544-doacao-de-cadeiras-de-rodas-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/fake-news-cadeira-de-rodas.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45544-doacao-de-cadeiras-de-rodas-e-fake-news">Doação de cadeiras de rodas - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Doação de cadeiras de rodas - É FAKE NEWS!              <p>Olá, essa notícia é
 falsa! Não compartilhe! O texto contém características de Fake News, 
como erro de gramática, alarmista, informações vagas, não há datas e 
fontes confiáveis...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 24/06/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 18h22</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45542-oms-reclassifica-conceito-de-jovem-idoso-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/FakeNews-OMS-reclassifica.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45542-oms-reclassifica-conceito-de-jovem-idoso-e-fake-news">OMS reclassifica conceito de jovem/idoso - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                OMS reclassifica conceito de jovem/idoso - É FAKE NEWS!             <p>Olá, 
essa notícia é falsa! Não compartilhe! O texto contém características de
 Fake News, como erro de gramática, alarmista, informações vagas, não há
 datas e fontes confiáveis...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 24/06/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h56</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45453-ondas-radioativas-do-microondas-causam-danos-a-saude-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News--governo-japoes.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45453-ondas-radioativas-do-microondas-causam-danos-a-saude-e-fake-news">Ondas radioativas do microondas causam danos à saúde - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Ondas radioativas do microondas causam danos à saúde - É FAKE NEWS!             <p>Olá!
 Essa mensagem é falsa! Não compartilhe! Não há evidências científicas 
do que foi exposto no texto. Há erros de gramática e o texto tem caráter
 alarmista, características de...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 20/05/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h20</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45354-vazamento-de-dados-do-datasus-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/fake-datasus.jpg" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45354-vazamento-de-dados-do-datasus-e-fake-news">Vazamento de dados do DATASUS - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Vazamento de dados do DATASUS - É FAKE NEWS!                <p>O Ministério da 
Saúde tem implementado processos cada vez mais rígidos para a 
identificação dos profissionais que acessam diariamente os sistemas de 
informação, objetivando coibir...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 11/04/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 14h47</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45276-alimentos-e-a-cura-do-cancer-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-dicas-gerais.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45276-alimentos-e-a-cura-do-cancer-e-fake-news">Alimentos e a cura do câncer - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Alimentos e a cura do câncer - É FAKE NEWS!             <p>Olá, não 
compartilhe essa mensagem, contém informação falsa! Apesar deste texto 
ter algumas recomendações verdadeiras, não há fontes. Existem diversas 
informações vagas e erros...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 28/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h42</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45275-barras-em-embalagens-indicam-que-o-leite-esta-vencido-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-leite.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45275-barras-em-embalagens-indicam-que-o-leite-esta-vencido-e-fake-news">Barras em embalagens indicam que o leite está vencido - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Barras em embalagens indicam que o leite está vencido - É FAKE NEWS!                <p>Olá!
 Não compartilhe este vídeo, ele é falso! Este viral foi compartilhado 
como vídeo e imagem – ambas afirmando que as barrinhas indicavam que o 
leite estaria vencido e sendo...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 28/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h41</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45271-furar-dedos-com-agulha-ajuda-a-salvar-pessoa-com-avc-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-AGULHA-AVC.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45271-furar-dedos-com-agulha-ajuda-a-salvar-pessoa-com-avc-e-fake-news">Furar dedos com agulha ajuda a salvar pessoa com AVC - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Furar dedos com agulha ajuda a salvar pessoa com AVC - É FAKE NEWS!             <p>Olá!
 Essa mensagem é falsa! Não compartilhe. Não há nenhuma comprovação 
científica que furar os dedos de uma pessoa a ajudaria em caso de 
Acidente Vascular Cerebral. O tratamento...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 28/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 11h07</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45270-repelente-de-insetos-causa-reacao-quimica-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News--total-expert.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45270-repelente-de-insetos-causa-reacao-quimica-e-fake-news">Repelente de insetos causa reação química - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Repelente de insetos causa reação química - É FAKE NEWS!                <p>Olá! 
Essa mensagem é falsa, não compartilhe! Conforme esclarecimentos 
prestados pela fabricante do produto, a partir de testes de eficácia e 
segurança do produto, o uso do repelente...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 28/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 11h06</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45265-ar-condicionado-e-o-benzeno-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-benzeno.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45265-ar-condicionado-e-o-benzeno-e-fake-news">Ar condicionado e o benzeno - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Ar condicionado e o benzeno - É FAKE NEWS!              <p>Olá, essa mensagem é
 falsa! Não compartilhe. Os níveis da substância em carros é 
extremamente baixa, não sendo prejudicial à saúde. De fato, o benzeno é 
usado na fabricação dos...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 27/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h45</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45264-equinocio-e-altas-temperaturas-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Fake-News-equinocio.jpeg" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45264-equinocio-e-altas-temperaturas-e-fake-news">Equinócio e altas temperaturas - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Equinócio e altas temperaturas - É FAKE NEWS!               <p>Olá, essa 
mensagem é falsa! Não compartilhe! A mensagem tem caráter alarmista, não
 cita fontes e tem informações vagas - não fala em datas com exatidão e 
pede compartilhamento,...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 27/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h44</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45244-planta-caseira-causa-morte-de-crianca-de-5-anos-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-planta.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45244-planta-caseira-causa-morte-de-crianca-de-5-anos-e-fake-news">Planta caseira causa morte de criança de 5 anos - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Planta caseira causa morte de criança de 5 anos - É FAKE NEWS!              <p>Olá,
 essa mensagem é falsa! Não compartilhe! A história surgiu em outros 
países, com&nbsp; outros nomes e com mudanças de nomes de cidades.
Também é possível conferir na imagem as...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 21/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h40</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45243-mamografia-causa-cancer-de-tireoide-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-cancer-radiografia.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45243-mamografia-causa-cancer-de-tireoide-e-fake-news">Mamografia causa câncer de tireoide - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Mamografia causa câncer de tireoide - É FAKE NEWS!              <p>Olá! Não 
compartilhe este vídeo! Ele é falso! O próprio Dr. Drauzio Varella veio a
 público desmentir esta moça que alega que ele teria afirmando que o 
câncer de tireoide tem...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 21/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h11</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45240-tratamento-de-queimaduras-com-farinha-de-trigo-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-farinha-queimada.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45240-tratamento-de-queimaduras-com-farinha-de-trigo-e-fake-news">Tratamento de queimaduras com farinha de trigo - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Tratamento de queimaduras com farinha de trigo - É FAKE NEWS!               <p>Olá!
 Não compartilhe essa mensagem, ela é falsa! A mensagem sobre tratamento
 de queimaduras com farinha de trigo. Não há estudos científicos sobre 
esse tratamento, e não há...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 20/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h49</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45239-aftas-sao-a-causa-do-cancer-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SSFN--c--ncer-medico-italiano.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45239-aftas-sao-a-causa-do-cancer-e-fake-news">Aftas são a causa do câncer - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Aftas são a causa do câncer - É FAKE NEWS!              <p>Olá! Não 
compartilhe essa mensagem! A notícia é falsa. Os pacientes com câncer 
têm realmente infecções oportunistas com mais frequência, incluindo por 
fungos. Estas infecções...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 20/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h46</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45238-doacao-de-caixa-de-medicamento-quimioterapico-para-leucemia-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/C--pia-de-SS-Fake-News-remedio.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45238-doacao-de-caixa-de-medicamento-quimioterapico-para-leucemia-e-fake-news">Doação de caixa de medicamento quimioterápico para leucemia - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Doação de caixa de medicamento quimioterápico para leucemia - É FAKE NEWS!              <p>Olá!
 Essa mensagem é falsa! Não compartilhe! A mensagem não informa quem 
está doando, o local, o contato, ou seja, informações vagas - que são 
características de Fake News. Além...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 20/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h45</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45232-falta-de-pacientes-para-transplante-de-corneas-em-sorocaba-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-cornea.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45232-falta-de-pacientes-para-transplante-de-corneas-em-sorocaba-e-fake-news">Falta de pacientes para transplante de córneas em Sorocaba - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Falta de pacientes para transplante de córneas em Sorocaba - É FAKE NEWS!               <p>Olá,
 essa mensagem é falsa! Não compartilhe! A mensagem tem caráter 
alarmista, pede compartilhamento, e circula na internet há bastante 
tempo - características de Fake News. Além...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 18/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h35</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45223-limao-no-copo-mata-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-lim--o-no-copo.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45223-limao-no-copo-mata-e-fake-news">Limão no copo mata - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Limão no copo mata - É FAKE NEWS!               <p>Olá! Essa mensagem é falsa, 
não compartilhe! Além de ter caráter alarmista, apelam para o lado 
emocional, pedem compartilhamento e&nbsp; essa mensagem circula, pelo 
menos, desde 2004...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 15/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 10h46</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45222-onda-de-calor-sensacao-termica-de-55-c-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-ondas-de-calor.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45222-onda-de-calor-sensacao-termica-de-55-c-e-fake-news">Onda de calor - sensação térmica de 55ºC - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Onda de calor - sensação térmica de 55ºC - É FAKE NEWS!             <p>É 
falso texto que afirma que há uma previsão de onda de calor atingindo o 
Brasil. O texto contém&nbsp; todos as características de Fake News, 
alarmista, pede compartilhamento, fontes...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 15/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 10h45</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45221-aids-e-bananas-mutamba-e-roupas-brancas-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/fake-news.jpg" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45221-aids-e-bananas-mutamba-e-roupas-brancas-e-fake-news">Aids e bananas, mutamba e roupas brancas - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Aids e bananas, mutamba e roupas brancas - É FAKE NEWS!             <p>Olá, 
essa mensagem é falsa! Não compartilhe! Ela tem caráter alarmante, pede 
compartilhamento, não informa o local - cidade, não tem fonte, todas 
características de uma Fake News. O...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 15/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 10h43</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45209-paracetamol-aumenta-riscos-de-autismo-ou-tdah-nas-criancas-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-parecetamol.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45209-paracetamol-aumenta-riscos-de-autismo-ou-tdah-nas-criancas-e-fake-news">Paracetamol aumenta riscos de autismo ou TDAH nas crianças - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Paracetamol aumenta riscos de autismo ou TDAH nas crianças - É FAKE NEWS!               <p>Olá! Essa mensagem é falsa por não ser conclusivo os estudos. Entenda:
De fato, o artigo citado na reportagem *sugere o aumento de risco de paralisia cerebral com o uso da aspirina e...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 12/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h53</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45208-uso-de-celular-na-cozinha-e-acidentes-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-n--o-use-celular-na-cozinha.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45208-uso-de-celular-na-cozinha-e-acidentes-e-fake-news">Uso de celular na cozinha e acidentes - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Uso de celular na cozinha e acidentes - É FAKE NEWS!                <p>Não 
compartilhe essa mensagem, ela é falsa! Contém todas as características 
de Fake News, tom alarmista, erro de português e pede compartilhamento. A
 fonte citada no texto não existe...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 12/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h35</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45206-exercicio-com-a-lingua-previne-alzheimer-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-alzheimer.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45206-exercicio-com-a-lingua-previne-alzheimer-e-fake-news">Exercício com a língua previne Alzheimer - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Exercício com a língua previne Alzheimer - É FAKE NEWS!             <p>Olá, 
essa mensagem é falsa. Essa mensagem circula há alguns anos, e tem 
origem no exterior, tendo sido traduzida para o português e viralizado 
em 2018. Não há estudos científicos...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 12/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h07</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45199-dia-d-de-vacinacao-contra-sarampo-em-16-02-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-sarampo.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45199-dia-d-de-vacinacao-contra-sarampo-em-16-02-e-fake-news">Dia D de vacinação contra sarampo em 16/02 - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Dia D de vacinação contra sarampo em 16/02 - É FAKE NEWS!               <p>O 
Ministério da Saúde adverte que a imagem que circula nas redes sociais 
anunciando um Dia D Nacional de vacinação no dia 16 de fevereiro é 
falsa! Não compartilhe!
O cartaz se refere...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 08/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 18h27</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45185-cientistas-israelenses-e-a-cura-do-cancer-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News-CANCER-ISRAELENSES-CURA.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45185-cientistas-israelenses-e-a-cura-do-cancer-e-fake-news">Cientistas israelenses e a cura do câncer - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Cientistas israelenses e a cura do câncer - É FAKE NEWS!                <p>Essa 
notícia é falsa! Não compartilhe!&nbsp; A&nbsp;iniciativa é um esforço 
de uma empresa que não foi sequer testada clinicamente ainda. Não há 
qualquer evidência sólida...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 06/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 10h04</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45183-10-razoes-pelas-quais-nao-deveria-vacinar-seu-filho-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News--10-raz--es-vacina.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45183-10-razoes-pelas-quais-nao-deveria-vacinar-seu-filho-e-fake-news">10 razões pelas quais não deveria vacinar seu filho - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                10 razões pelas quais não deveria vacinar seu filho - É FAKE NEWS!              <p>*Olá!
 Não compartilhe essa notícia, ela é falsa! O texto que circula nas 
redes sociais, sobre as 10 razões pelas quais não deveria vacinar seu 
filho é cheio de inverdades e com...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 05/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 18h06</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45181-cofen-proibe-registro-de-diplomas-de-cursos-ead-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/cofen.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45181-cofen-proibe-registro-de-diplomas-de-cursos-ead-e-fake-news">COFEN proíbe registro de diplomas de cursos EAD - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                COFEN proíbe registro de diplomas de cursos EAD - É FAKE NEWS!              <p>Olá,
 não compartilhe essa mensagem. Ela é falsa! Na realidade, o Conselho 
Federal de Farmácia (CFF), que decidiu pela proibição de inscrição e o 
registro pelos Conselhos Regionais...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 05/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h06</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45180-cirurgia-de-labio-leporino-no-hospital-militar-de-curitiba-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/878a6dc7-0109-4ec4-b07f-6d108b899f05.jpg" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45180-cirurgia-de-labio-leporino-no-hospital-militar-de-curitiba-e-fake-news">Cirurgia de lábio leporino no Hospital Militar de Curitiba - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Cirurgia de lábio leporino no Hospital Militar de Curitiba - É FAKE NEWS!               <p>Olá!
 Não compartilhe essa mensagem, ela é falsa. Além de ter todas as 
características de Fake news, como tom alarmistas, erros de português e 
imprecisão em datas, essa mensagem tem...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 05/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h38</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45178-fevereiro-mais-quente-da-historia-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/SS-Fake-News---Fortes-ondas-de-calor.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45178-fevereiro-mais-quente-da-historia-e-fake-news">Fevereiro mais quente da história - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Fevereiro mais quente da história - É FAKE NEWS!                <p>Olá! Não 
compartilhe essa mensagem, ela é falsa. A mensagem tem caráter 
alarmista, pede compartilhamento e apresenta fontes falsa – o que indica
 ser Fake News. E o INMET divulgou uma...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 05/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h35</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45174-frutas-e-a-cura-do-cancer-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/fake-news-fruta.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45174-frutas-e-a-cura-do-cancer-e-fake-news">Frutas e a cura do câncer - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Frutas e a cura do câncer - É FAKE NEWS!                <p>A notícia é falsa. 
Não há evidência científica de que comer frutas após as refeições, 
aquecidas ou cozidas piorem a oferta de nutrientes das frutas. As 
principais instituições...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 01/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h41</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45173-fechamento-do-hospital-do-homem-sp-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/FAKE-NEWS-HOSPITAL-DO-HOMEM.jpg" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45173-fechamento-do-hospital-do-homem-sp-e-fake-news">Fechamento do Hospital do Homem/SP - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Fechamento do Hospital do Homem/SP - É FAKE NEWS!               <p>Olá, essa 
mensagem é falsa. Conferindo em portais de checadores de notícias 
pudemos conferir que esse viral circula desde 2015, ano em que a própria
 instituição citada no texto veio...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 01/02/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 13h58</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45160-gelo-causa-cancer-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/gelo-cancer.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45160-gelo-causa-cancer-e-fake-news">Gelo causa câncer - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Gelo causa câncer - É FAKE NEWS!                <p>Olá, não compartilhe essa 
mensagem! Ela é falsa! Não há nenhum nexo científico nas afirmações. 
Trata-se de uma afirmativa falsa, não há relação entre consumir gelo em 
qualquer...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 31/01/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h30</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45159-cancer-e-deficiencia-da-vitamina-b17-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/vitamina-c--ncer.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45159-cancer-e-deficiencia-da-vitamina-b17-e-fake-news">Câncer é deficiência da vitamina B17 - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Câncer é deficiência da vitamina B17 - É FAKE NEWS!             <p>O conteúdo
 da mensagem é falso. O complexo vitamínico B inclui as vitaminas B1, 
B2, B3, B5, B6, B7, B9 e B12. O complexo vitamínico B é um grupo de 
nutrientes que exercem importantes...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 31/01/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h29</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45158-cura-do-cancer-por-medico-militar-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Cura-do-C--ncer-por-m--dico-militar-fake.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45158-cura-do-cancer-por-medico-militar-e-fake-news">Cura do câncer por médico militar - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Cura do câncer por médico militar - É FAKE NEWS!                <p>Olá, essa 
mensagem é falsa! Não compartilhe! Ela tem todas as características de 
Fake News, erros de português, caráter alarmista, pede compartilhamento.
 O Instituto Nacional do...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 31/01/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h27</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45157-estudo-associa-omeprazol-com-tumores-no-estomago-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Omeprazol-fakenews.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45157-estudo-associa-omeprazol-com-tumores-no-estomago-e-fake-news">Estudo associa Omeprazol com tumores no estômago - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Estudo associa Omeprazol com tumores no estômago - É FAKE NEWS!             <p>Essa
 notícia é falsa! Não compartilhe. A afirmação de que remédio para 
gastrite, úlcera e refluxo dobra o risco de câncer implica uma relação 
de causa e efeito. Entretanto, o...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 31/01/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 11h20</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45155-novas-regras-para-consulta-medica-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/CFM-FakeNews.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45155-novas-regras-para-consulta-medica-e-fake-news">Novas regras para consulta médica - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Novas regras para consulta médica - É FAKE NEWS!                <p>“O 
atendimento presencial e direto do médico em relação ao paciente é regra
 para a boa prática médica, conforme dispõe o artigo 37 do Código de 
Ética Médica: “É vedado ao...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 31/01/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 10h32</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45154-nova-gripe-fatal-e-cha-de-erva-doce-e-fake-news">
                        <img class="tileImage" src="Fake%20News_files/FakeNews-ervadoce.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45154-nova-gripe-fatal-e-cha-de-erva-doce-e-fake-news">Nova gripe fatal e chá de erva doce - É FAKE NEWS!</a>
            </h2>
            <span class="description">
                Nova gripe fatal e chá de erva doce - É FAKE NEWS!              <p>Olá! Não 
compartilhe essa mensagem! É falsa! O Hospital das Clínicas de São Paulo
 esclareceu que não realizou alertas à população sobre um suposto vírus 
da gripe que se...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 31/01/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 10h28</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45153-vacina-faz-mal-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Vacina_fake_news_video.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45153-vacina-faz-mal-fake-news">Vacina faz mal - Fake News!</a>
            </h2>
            <span class="description">
                Vacina faz mal - Fake News!             <p>Olá, não compartilhe esse vídeo! 
Ele tem diversas informações falsas! Esse vídeo&nbsp; divulga 
informações&nbsp; inverídicas a respeito da vacina.
O ditado popular “melhor...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 30/01/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h53</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45152-epidemia-de-aranhas-marrom-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Epidemia_de_aranhas_marrom_fakenews.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45152-epidemia-de-aranhas-marrom-fake-news">Epidemia de aranhas marrom - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Epidemia de aranhas marrom - FAKE NEWS!             <p>Olá! O áudio sobre 
aranhas marrom tem caráter alarmista e informações falsas. Contudo, vale
 ressaltar que os acidentes causados por aranhas são comuns, porém a 
maioria não...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 30/01/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h51</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45122-vagas-com-entrevista-marcada-na-upa-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Fake_News-contratao_UPA.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45122-vagas-com-entrevista-marcada-na-upa-fake-news">Vagas com entrevista marcada na UPA - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Vagas com entrevista marcada na UPA - FAKE NEWS!                <p>Essa 
informação é falsa! Não compartilhe! Esse boato está circulando com 
outras formas, como contratação para o SAMU. E além disso, o link 
compartilhado é falso! Para saber sobre...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 15/01/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h05</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/45081-cadastro-no-brasil-sorridente-fake-news">
                        <img class="tileImage" src="Fake%20News_files/FAKE_NEWS__Brasil_sorridente.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/45081-cadastro-no-brasil-sorridente-fake-news">Cadastro no Brasil Sorridente - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Cadastro no Brasil Sorridente - FAKE NEWS!              <p>Olá! Não 
compartilhe essa mensagem, pois ela é falsa! Esse viral está divulgando 
um site falso que funciona como "phising", isto é, roubo de dados. Para 
ser atendido pelo programa...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 07/01/19</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h13</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44875-agua-gelada-faz-mal-fake-news">
                        <img class="tileImage" src="Fake%20News_files/agua_gelada_faz_mal.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44875-agua-gelada-faz-mal-fake-news">Água gelada faz mal - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Água gelada faz mal - FAKE NEWS!                <p>Essa mensagem é falsa! Não 
compartilhe. Além de atribuir o texto ao Dr. Dráuzio Varella com uma 
especialidade diferente da dele, o texto contém diversas informações 
falsas e...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 05/12/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h27</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44874-oleo-no-umbigo-cura-doencas-fake-news">
                        <img class="tileImage" src="Fake%20News_files/leo_no_umbigo_cura_doenas.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44874-oleo-no-umbigo-cura-doencas-fake-news">Óleo no umbigo cura doenças - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Óleo no umbigo cura doenças - FAKE NEWS!                <p>Olá, essa mensagem 
não passa de mais um boato! Não há efetivamente uma fórmula mágica para a
 cura de todas as doenças, como ressalta o Boatos.org, parceiro do 
Ministério da Saúde...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 05/12/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h21</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44873-quiabo-cura-diabetes-fake-news">
                        <img class="tileImage" src="Fake%20News_files/quiabo_cura_diabetes.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44873-quiabo-cura-diabetes-fake-news">Quiabo cura diabetes - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Quiabo cura diabetes - FAKE NEWS!               <p>Olá, não compartilhe essa 
mensagem, ela falsa! A SBD (Sociedade Brasileira de Diabetes) emitiu um 
alerta sobre essa suposta cura para o diabetes. Para a entidade, existe 
uma grande...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 05/12/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h19</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44872-guardar-cebola-cortada-e-altamente-perigoso-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Guardar_cebola_cortada_altamente_perigoso.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44872-guardar-cebola-cortada-e-altamente-perigoso-fake-news">Guardar cebola cortada é altamente perigoso - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Guardar cebola cortada é altamente perigoso - FAKE NEWS!                <p>Olá! 
Não compartilhe essa mensagem, ela é falsa! A Sociedade Brasileira de 
Infectologia divulgou uma nota afirmando que a Dra Marinella Della 
Negro, citada como autora do áudio,...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 05/12/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h13</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44771-refrigerantes-falta-de-atividade-renal-e-tumores-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Fake_NEWS-REFRI.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44771-refrigerantes-falta-de-atividade-renal-e-tumores-fake-news">Refrigerantes, falta de atividade renal e tumores - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Refrigerantes, falta de atividade renal e tumores - FAKE NEWS!              <p>Olá!
 Essa mensagem é falsa. Não a compartilhe. A Sociedade Brasileira de 
Cardiologia já desmentiu essa mensagem que circula, pelo menos, desde 
2006 - com modificações. O Boatos.org,...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 26/11/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 12h21</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44721-agua-quente-de-coco-e-cura-do-cancer-fake-news">
                        <img class="tileImage" src="Fake%20News_files/coco_quente_fakenews.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44721-agua-quente-de-coco-e-cura-do-cancer-fake-news">Água quente de coco e cura do câncer - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Água quente de coco e cura do câncer - FAKE NEWS!               <p>Essa 
mensagem é falsa! Não compartilhe! Não existe um alimento específico ou 
milagroso para a prevenção e/ou cura do câncer. Não existem evidências 
científicas que atribuam tal...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 22/11/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h27</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44714-cura-do-cancer-por-alimentos-milagrosos-fake-news">
                        <img class="tileImage" src="Fake%20News_files/FakeNews_cncer.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44714-cura-do-cancer-por-alimentos-milagrosos-fake-news">Cura do câncer por alimentos milagrosos - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Cura do câncer por alimentos milagrosos - FAKE NEWS!                <p>Olá! O 
conteúdo da mensagem é falso. Apesar da redução do consumo de açúcar ser
 benéfica para a saúde e para a prevenção do câncer, uma vez que a 
doença está instalada, não...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 21/11/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h06</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44658-besouros-que-causam-cegueira-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Besouro_fakenews.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44658-besouros-que-causam-cegueira-fake-news">Besouros que causam cegueira - FAKE NEWS</a>
            </h2>
            <span class="description">
                Besouros que causam cegueira - FAKE NEWS                <p>Olá! Essa mensagem é 
falsa! Não compartilhe. Não é verdade que um besouro potó deixou um 
homem cego depois de entrar em seu ouvido. O Boatos.org, parceiro do 
Ministério da Saúde,...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 09/11/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h22</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44623-limonada-quente-cura-o-cancer-fake-news">
                        <img class="tileImage" src="Fake%20News_files/limonada_fakenews.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44623-limonada-quente-cura-o-cancer-fake-news">Limonada quente cura o câncer - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Limonada quente cura o câncer - FAKE NEWS!              <p>Essa mensagem é 
falsa! Não compartilhe! Beber água com limão não mata células 
cancerígenas.&nbsp; Não existe um alimento específico ou milagroso para a
 prevenção e/ou cura do...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 08/11/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h47</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44525-contrato-emergencial-do-samu-sem-experiencia-fake-news">
                        <img class="tileImage" src="Fake%20News_files/FAKE_NEWS_SAMU.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44525-contrato-emergencial-do-samu-sem-experiencia-fake-news">Contrato emergencial do SAMU sem experiência - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Contrato emergencial do SAMU sem experiência - FAKE NEWS!               <p>Essa
 informação é falsa! Não compartilhe!
Segundo boato, o Serviço de Atendimento Móvel de Urgência (SAMU) estaria
 contratando de forma emergencial, profissionais sem experiência....</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 17/10/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h43</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44466-paracetamol-e-virus-machupo-fake-news">
                        <img class="tileImage" src="Fake%20News_files/FakeNews_Machupo.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44466-paracetamol-e-virus-machupo-fake-news">Paracetamol e vírus Machupo - FAKE NEWS</a>
            </h2>
            <span class="description">
                Paracetamol e vírus Machupo - FAKE NEWS             <p>Olá! Essa notícia é 
falsa! Não compartilhe!&nbsp; A Anvisa informa que a confiabilidade dos 
medicamentos é assegurada por meio da definição de rígidos critérios de 
qualidade...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 04/10/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 18h20</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44462-cha-de-folhas-de-graviola-cura-o-cancer-fake-news">
                        <img class="tileImage" src="Fake%20News_files/FakeNews_FolhadeGraviola.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44462-cha-de-folhas-de-graviola-cura-o-cancer-fake-news">Chá de folhas de graviola cura o câncer - FAKE NEWS</a>
            </h2>
            <span class="description">
                Chá de folhas de graviola cura o câncer - FAKE NEWS             <p>Essa 
mensagem é falsa! Não compartilhe! Não há evidências científicas de que o
 chá de folhas de graviola cure o câncer. O próprio médico citado na 
mensagem desmentiu essa...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 03/10/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h54</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44441-hospital-mario-kroeff-e-mamografia-fake-news">
                        <img class="tileImage" src="Fake%20News_files/FakeNews_OutubroRosa.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44441-hospital-mario-kroeff-e-mamografia-fake-news">Hospital Mário Kroeff e mamografia - FAKE NEWS</a>
            </h2>
            <span class="description">
                Hospital Mário Kroeff e mamografia - FAKE NEWS              <p>Não compartilhe
 essa mensagem! É Fake News! O próprio Hospital Mário Kroeff já 
desmentiu essa informação, que começou a circular em setembro do ano. 
Não há realização de...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 27/09/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 14h13</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44429-vacinas-causam-autismo-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Vacina_causa_autismo_fake.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44429-vacinas-causam-autismo-fake-news">Vacinas causam autismo - FAKE NEWS</a>
            </h2>
            <span class="description">
                Vacinas causam autismo - FAKE NEWS              <p>Fake News! Um estudo 
apresentado em 1998, que levantou preocupações sobre uma possível 
relação entre a vacina contra o sarampo, a caxumba e a rubéola e o 
autismo, foi posteriormente...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 24/09/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h23</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44425-beber-agua-antes-de-pintar-o-cabelo-fake-news">
                        <img class="tileImage" src="Fake%20News_files/FAKE_NEWS__BEBER_AGUA_ANTES_DE_PINTAR_O_CABELO.jpg" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44425-beber-agua-antes-de-pintar-o-cabelo-fake-news">Beber água antes de pintar o cabelo - FAKE NEWS!</a>
            </h2>
            <span class="description">
                Beber água antes de pintar o cabelo - FAKE NEWS!                <p>Garantir que a
 ingestão de água durante “todo o tempo de ação do produto, manter a 
bexiga cheia e só esvaziar após lavar os cabelos” como forma de 
precaução “para que as...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 21/09/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h16</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44324-uso-do-celular-no-escuro-e-cancer-de-olho-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Maculopatia.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44324-uso-do-celular-no-escuro-e-cancer-de-olho-fake-news">Uso do celular no escuro e câncer de olho - FAKE NEWS</a>
            </h2>
            <span class="description">
                Uso do celular no escuro e câncer de olho - FAKE NEWS               <p>O texto intitulado USO DO CELULAR NO ESCURO está repleto de informações equivocadas e sem comprovação científica.
Não existem estudos científicos mostrando que o uso do celular,...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 06/09/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h10</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44322-cura-do-diabetes-com-capsula-natural-fake-news">
                        <img class="tileImage" src="Fake%20News_files/fake_news_diabetes.jpg" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44322-cura-do-diabetes-com-capsula-natural-fake-news">Cura do diabetes com cápsula natural - FAKE NEWS</a>
            </h2>
            <span class="description">
                Cura do diabetes com cápsula natural - FAKE NEWS                <p>Este site é 
falso e a mensagem também! Portanto é uma Fake News, não compartilhe! 
Muitos sites publicadores de fake News têm nomes parecidos com endereços
 de sites de notícias....</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 05/09/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 17h45</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44289-peste-negra-ameaca-voltar-a-paraiba-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Peste.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44289-peste-negra-ameaca-voltar-a-paraiba-fake-news">"Peste Negra" ameaça voltar à Paraíba - FAKE NEWS</a>
            </h2>
            <span class="description">
                "Peste Negra" ameaça voltar à Paraíba - FAKE NEWS               <p>O Brasil não
 registra casos de peste humana desde 2005, entretanto, existem no país 
áreas em que há a confirmação da circulação da Yersínia pestis - 
bactéria responsável pela...</p>            </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 05/09/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 11h13</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44248-vacinas-obrigatorias-o-que-ha-por-tras-disso-elas-sao-confiaveis">
                        <img class="tileImage" src="Fake%20News_files/Vacinas-obrigatorias-.jpg" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44248-vacinas-obrigatorias-o-que-ha-por-tras-disso-elas-sao-confiaveis">Vacinas obrigatórias - FAKE NEWS</a>
            </h2>
            <span class="description">
                Vacinas obrigatórias - FAKE NEWS                <p>Esse portal profere bastante 
inverdades a respeito da vacina. Portanto, é uma Fake News! Não 
compartilhe. O ditado popular “melhor prevenir do que remediar” se 
aplica perfeitamente...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 03/09/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 10h51</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44237-coletes-de-agentes-endemicos-de-controle-da-dengue-roubados-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Coletes_roubados_.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44237-coletes-de-agentes-endemicos-de-controle-da-dengue-roubados-fake-news">Coletes de agentes endêmicos de controle da dengue roubados - FAKE NEWS</a>
            </h2>
            <span class="description">
                Coletes de agentes endêmicos de controle da dengue roubados - FAKE NEWS             <p>Esse
 boato já foi desmentido por um de nossos parceiros, o Boatos.org. Ela 
circula desde 2015 e se espalhou por diversas cidades, não há 
comprovação que existam quadrilhas em diversas...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 30/08/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 18h51</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44234-vacina-anticancer-fake-news">
                        <img class="tileImage" src="Fake%20News_files/vacina-cancer.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44234-vacina-anticancer-fake-news">Vacina anticâncer - FAKE NEWS</a>
            </h2>
            <span class="description">
                Vacina anticâncer - FAKE NEWS               <p>Não existe vacina anticâncer. O 
próprio Hospital Sírio-Libanês citado na mensagem já desmentiu essa Fake
 News, que circula desde 2008. A Secretaria de Vigilância em Saúde, 
do...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 30/08/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h38</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44193-bananas-com-virus-hiv-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Banana_com_vrus_hiv.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44193-bananas-com-virus-hiv-fake-news">Bananas com vírus HIV - FAKE NEWS</a>
            </h2>
            <span class="description">
                Bananas com vírus HIV - FAKE NEWS               <p>A banana não seria uma meio 
externo com condições propícias para transmissão do vírus do HIV, assim 
como não há chance de contrair o HIV por contato com roupas, objetos 
(copos,...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 29/08/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 18h38</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44192-efeitos-da-glandula-da-prostata-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Prstata.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44192-efeitos-da-glandula-da-prostata-fake-news">Efeitos da glândula da próstata - FAKE NEWS</a>
            </h2>
            <span class="description">
                Efeitos da glândula da próstata - FAKE NEWS             <p>A notícia que 
circula nas redes sociais sobre os efeitos da glândula da próstata na 
saúde dos homens é falsa. De acordo com o Dr. Franz Campos, Chefe da 
Seção de Urologia do INCA, a...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 29/08/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 16h45</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44190-bacterias-nos-feijoes-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Feijo_com_bactria_.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44190-bacterias-nos-feijoes-fake-news">Bactérias nos feijões - FAKE NEWS</a>
            </h2>
            <span class="description">
                Bactérias nos feijões - FAKE NEWS               <p>A Fiocruz esclarece que, de 
acordo com as mensagens veiculadas, “nem mesmo água fervente poderia 
eliminar o microrganismo e só seria possível fazê-lo deixando o feijão 
submerso em...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 29/08/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 15h54</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44186-novo-dipirona-importado-da-venezuela-contem-virus-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Dipirona.jpg" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44186-novo-dipirona-importado-da-venezuela-contem-virus-fake-news">Novo dipirona importado da Venezuela contém vírus - FAKE NEWS</a>
            </h2>
            <span class="description">
                Novo dipirona importado da Venezuela contém vírus - FAKE NEWS               <p>A
 Agência Nacional de Vigilância Sanitária (Anvisa) afirma que a notícia 
que está circulando nas redes sociais sobre a dipirona importada da 
Venezuela conter o vírus "Marbug" é...</p>          </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 29/08/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 11h20</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44145-jovem-sus-fake-news">
                        <img class="tileImage" src="Fake%20News_files/Jovem_SUS.jpeg" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44145-jovem-sus-fake-news">Jovem SUS - FAKE NEWS</a>
            </h2>
            <span class="description">
                Jovem SUS - FAKE NEWS               <p>ESSA NOTÍCIA É FALSA, NÃO COMPARTILHE! A
 imagem é antiga! De agosto de 2015. A prefeitura de São Paulo promoveu o
 Projeto Jovem SUS até o ano de 2017.&nbsp; É possível confirmar...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 28/08/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 11h33</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44144-japao-vacina-contra-o-hpv-sob-julgamento-devido-a-horriveis-efeitos-colaterais-fake-news">
                        <img class="tileImage" src="Fake%20News_files/2.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44144-japao-vacina-contra-o-hpv-sob-julgamento-devido-a-horriveis-efeitos-colaterais-fake-news">Japão: vacina contra o HPV sob julgamento devido a horríveis efeitos colaterais - FAKE NEWS</a>
            </h2>
            <span class="description">
                Japão: vacina contra o HPV sob julgamento devido a horríveis efeitos colaterais - FAKE NEWS             <p>Não
 existe e nunca existiu a proibição da vacina HPV (Papilomavírus Humano)
 mencionada na imagem. O Ministério da Saúde esclarece que essa vacina é
 segura e eficaz e, assim como...</p>           </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 28/08/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 10h45</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->

        <div class="tileItem">

            <!-- SPAN9 -->
            <div class="span9 tileContent">
                                <div class="tileImage">
                    <a href="http://www.saude.gov.br/fakenews/44143-mpf-proibe-vacina-contra-hpv-fake-news">
                        <img class="tileImage" src="Fake%20News_files/1.png" alt="" width="128" height="86">
                    </a>
                </div>
            
            <span class="subtitle"></span>
            <h2 class="tileHeadline">
                <a href="http://www.saude.gov.br/fakenews/44143-mpf-proibe-vacina-contra-hpv-fake-news">MPF proíbe vacina contra HPV - FAKE NEWS</a>
            </h2>
            <span class="description">
                MPF proíbe vacina contra HPV - FAKE NEWS                <p>Não existe e nunca 
existiu a proibição da vacina HPV (Papilomavírus Humano) mencionada na 
imagem. O Ministério da Saúde esclarece que essa vacina é segura e 
eficaz e, assim como...</p>         </span>

                                    Tags:   <div class="tags">
                                                                    <span class="tag-633 tag-list0">
                    <a href="http://www.saude.gov.br/component/tags/tag/fake-news" class="label label-info">
                        Fake News                   </a>
                </span>&nbsp;
                        </div>
            </div>

    <!-- SPAN3 -->
    <div class="span3 tileInfo">
        <ul>
            <li class="hide">publicado</li>
            <li><i class="icon-fixed-width icon-calendar"></i> 28/08/18</li>
            <li><i class="icon-fixed-width icon-time"></i> 10h42</li>
            <li><i class="icon-fixed-width icon-list"></i>&nbsp;<a href="http://www.saude.gov.br/fakenews">Fake News</a></li>
        </ul>
    </div>
</div>
<!-- div.tileItem -->
</div>
    </form></div>

"""


while var:

    #endereco = str(link) + '/' + str(pagina)

    endereco = html_doc

    print(endereco)

    #resposta = requests.get(endereco, headers=headers)    

    soup = BeautifulSoup(endereco, 'html.parser')
   
    try:
        for titulo in soup.find_all('h2',{'class':'tileHeadline'}):
            try:

                #print('TITULO:', titulo.getText())
                lista_titulo.append(titulo.getText())
            except:
                lista_titulo.append('NaN')

         
    except:
        continue
        '''
        Caso algo saia errado ou a página chegue
        ao final, o arquivo é gravado
        '''
    print(endereco)
    print('PAGINA: ', pagina)
          
    pagina-=1

    if pagina <= 90:
        break




#listass.to_csv('lista.csv')

csv = pd.DataFrame()

csv['titulo'] = lista_titulo


csv.to_csv('saude_gov_fake_news.csv')



'''
s1 = pd.Series(lista_titulo, name='titulo')
s2 = pd.Series(lista_corpo, name='corpo')
s3 = pd.Series(lista_url, name='url')

final = pd.concat([s1, s2, s3], axis=1)

final.to_csv('politica.csv')
'''