<?php

//creo la classe "Path", è il modello per generare sucessivamente la istanza dell'ogetto il percorso
class Path
{

//la classe "Path" ha una variabile/attributo $current_path che indica il percorso corrente
  public $current_path;

//  la classe "Path" ha la funzione costruttore, che viene invocata quando si usa l'operatore new.

// Il costruttore permette di eseguire azioni nel momento in cui viene creata l’istanza della classe.

  function __construct($path)
  {


    $this->current_path = $path;
  }


  //creo la funzione "cd" a cui passerò il parametro $new_path da cui dipenderà il cambiamento del percorso attuale ($current_path)
  public function cd($new_path)
  {

    //tutti i percorsi saranno salvati in un array, ogni percorso è un elemento singolo dell'array
    $dirs = array();

    //separo la stringa del nuovo percorso $new_path per elementi singoli con divisore "/"
    $new_dirs = explode('/', $new_path);

     //separo la stringa del percorso corrente per elementi singoli con divisore "/"
    $dirs = explode('/', $this->current_path);

    //cerco la prima occorrenza '/' della stringa $new_path
    $first_index = strstr($new_path, '/');


    //cerco la posizione della prima occorrenza '/' 
    $first_pos = strpos($new_path, '/');

    if ($first_index && $first_pos === 0) {
      $new_dirs = explode('/', $new_path);
      $dirs = array();
    }

 //attraverso array con le nuovi percorsi
    foreach ($new_dirs as $new_dir) {

      //se il nuovo percorso è uguale a '..' il  percorso "padre", allora devo estrarre un elemento dalla fine del array $dirs
      if ($new_dir === '..') {
        array_pop($dirs);
      }  else {
        //se il nuovo percorso ha qulcosa di nuovo faccio push nel array $dirs
        array_push($dirs, $new_dir);
      }
    }

    return implode('/', $dirs);
    //alla fine la funzione cd ritorna gli elementi dell'array come una stringa, ovvero un percorso dove tutti gli elementi sono separati da "/"
}



}
$path = new Path('/a/b/c/d');
$changed_path = $path->cd('../x');
echo $changed_path;


?>