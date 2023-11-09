//////////////////////////////////////////////////////////////////////////////
//
// INTERPOLATION CUBIQUE PAR INTERVALLE (PAR MORCEAUX)
//
// 
// 1) se donner N points (t(k),y(k)) avec t(1) < t(2) < ... < t(k-1) < t(k)
//
// 2) calculer la fonction cubique par morceaux qui interpole les donnees
//
// 3) puis tracer les donnees et la fonction dans une meme fenetre

    // ------------------ //
    // C-1 //
    t = [1  3  5  8 10 13];
    y = [2  3  7  8  3  1];
    
    // C-2 //
    // t = [1 3 4 6 8 9 10];
    // y = [37 20 15 12 10 10 10];
    
    
    // C-3 //
    // t = [0 %pi / 6 %pi / 3 %pi / 2 2 * %pi / 3 5 * %pi / 6 %pi];
    // y = [0 0.5 (3 ** 0.5) / 2 1 (3 ** 0.5) / 2 0.5 0 ];
        
    // nombre de donnees
    N = length(t);
    
    // -------------------------------------------------------------- //    
    // 2) calcul des N fonctions f_k avec 1 <= k <= N                 //
    // les 3 coefficients a_k, b_k et c_k definissant la fonction f_k //
    // sont stockees dans 3 vecteurs de taille N ainsi :              //
    // - un vecteur va contenant les differentes valeurs a_k          //
    //   va = [ a_1 a_2 ... a_N ]                                     //
    // - un vecteur vb contenant les differentes valeurs b_k          //
    //   vb = [ b_1 b_2 ... b_N ]                                     //
    // - un vecteur vc contenant les differentes valeurs c_k          //
    //   vc = [ c_1 c_2 ... c_N ]                                     //
    // et la fonction f_k est definie alors par l'expression          //
    //  f_k(t) = va(k) * t**2 + vb(k) * t + vc(k)                     //
    //                                                                //
    // -------------------------------------------------------------- //    
    
    // creation des vecteurs va, vb et vc avec N elements
    va = zeros(1,N);
    vb = zeros(1,N);
    vc = zeros(1,N);
    
    // determination des coefficients des N-2 fonctions f_k avec 2 <= k <= N-1
    for k=2:N-1
        // determination des 3 coefficients a,b,c de la fonction 
        // f_k(t) = a * t*t + b*t +c qui interpole
        // les 3 donnees (t(k-1),y(k-1)) , (t(k),y(k)) , (t(k+1),y(k+1)) :
        
        a = ( (y(k + 1) - y(k)) / (t(k + 1) - t(k)) - (y(k) - y(k - 1)) / (t(k) - t(k-1)) ) / (t(k + 1) - t(k-1))
        b = (y(k) - y(k - 1)) / (t(k) - t(k - 1)) - a * (t(k -1) + t(k))
        c = y(k-1) - a * (t(k -1) ** 2) - b * t(k -1)

        // - puis stocker les 3 coefficients dans les 3 vecteurs va, vb et nc 
        
        va(k) = a
        vb(k) = b
        vc(k) = c
        
    end
    
    // ajout des 2 fonctions f_1 = f_2 et f_N = f_N-1
    //  pour chaque vecteur va, vb et vc, copier le deuxieme element 
    //  le premier element, et l'avant-dernier element dans le dernier
    va(1) = va(2);   vb(1) = vb(2);   vc(1) = vc(2);
    va(N) = va(N-1); vb(N) = vb(N-1); vc(N) = vc(N-1);
        
    
    // --------------------------------------------------------- //    
    // 3) representation graphique des donnees et de la fonction //
    // --------------------------------------------------------- //    

    // creation de la fenetre graphique
    fid = scf()
    
    // representation des donnees sous forme de points rouges de taille 8
    plot(t,y,'r.','markersize',8)
        
    // representation de la fonction intervalle par intervalle
    for k=1:N-1
        
        // creer un tableau tt de 1000 points dans l'intervalle [t(k),t(k+1)]
        t1 = t(k);
        t2 = t(k+1);
        tt = linspace(t1,t2,1000);
        
        a1 = va(k)
        b1 = vb(k)
        c1 = vc(k)
        
        a2 = va(k + 1)
        b2 = vb(k + 1)
        c2 = vc(k + 1)
        
        deff("y = f_k(t)", "y = a1.*t.*t+b1.*t+c1")
        deff("y = f_k_plus(t)", "y = a2.*t.*t+b2*t+c2")
        deff("y = f(t)", "y = ((t2 - t) .* f_k(t) + (t - t1) .* f_k_plus(t)) ./ (t2 - t1)")

        plot(tt,f(tt),'k-','linewidth',2)
    end

