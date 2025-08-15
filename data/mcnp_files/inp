Titre : Hall CEZANE - Fichier Template
C ----------------------------------------
C 
C Fichier g�n�r� par INCA v3.0,
C le 25 avr. 2025 15:24:00
C 
C ----------------------------------------
C 
C CEZANE :
C     Densit� air : 0.0013
C     NPS : 150000
C     Mode : Neutron
C     BLOG : position retrait
C     CANEL : entroposage sud
C     Source Van Gogh Cf pr�difinie
C     Aucun c�ne d'ombre 
C     Aucun objet s�lection� sur T400 ni sur VanGogh
C     Chariot T400 :  distance 320.7
C                             altitude 0.0
C                             angle 0.0
C 
C     Chariot VanGogh :  distance 150.0
C                                    altitude 5.5
C                                    angle 0.0
C 
C Tallies :
C 
C ----------------------------------------
C --------------------------------------------------------------------------- C
C -----            Ce fichier contient les �l�ments suivants            ----- C
C  |-----------------------------------------------------------------------|  C
C  |        Element      | Cells / Surfs |      D�faut       | Disponibles |  C
C  |---------------------|---------------|-------------------|-------------|  C
C  | HALL CEZANE         |  5501 - 5750  |                   |             |  C
C  | PLATEFORME VAN GOGH |  5751 - 5875  |                   | 5876 - 5900 |  C
C  |                     |  5901 - 5981  |                   | 5982 - 6000 |  C
C  |                     |  6001 - 6143  |                   | 6144 - 6149 |  C
C  | PLATEFORME T400     |  6150 - 6269  |                   | 6270 - 6300 |  C
C  | LIGNE T400          |  6301 - 6423  |                   | 6424 - 6449 |  C
C  | BLOG                |  6450 - 6490  |      RETRAIT      | 6491 - 6499 |  C
C  | CANEL               |  6500 - 6578  |        SUD        | 6580 - 6600 |  C
C  | CHARIOT T400        |  6601 - 6647  |       RECUL�      | 6648 - 6700 |  C
C  | CHARIOT VAN GOGH    |  6700 - 6764  |       RECUL�      | 6764 - 6900 |  C
C  | ENCOMBREMENT HALL   |  6901 - 6958  |                   | 6959 - 7000 |  C
C  | BLOC SOURCE Cf/AmBe |  7001 - 7121  |  Cf mod�r� + Cd   | 7122 - .... |  C
C  |-----------------------------------------------------------------------|  C
C *************************************************************************** C
C *****     *****     REGLES DE GESTION DES CONFIGURATIONS    *****     ***** C
C *************************************************************************** C
C   Selon la configuration souhait�e, les �l�ments BLOG, CANEL, BLOC SOURCE   C
C   peuvent l�g�rement changer leur g�om�trie. Le pr�sent fichier est         C
C   param�tr� afin de faciliter l?insertion de ces �l�ments.                  C
C   M�me si en r�alit� ces �l�ments sont "int�gr�s" (toujours pr�sents dans   C
C   le fichier), ils sont con�us comme des pseudo-ins�rables:                 C
C   leurs d�finitions g�om�triques (cellules et surfaces) se trouvent dans    C
C   des fichiers � part. La m�thodologie d?insertion est la suivante:         C
C   1. Ces �l�ments sont marqu�s dans le fichier par des balises de type      C
C      "C INCA [NOM ELEMENT]".                                                C
C   2. Lors de la saisie via INCA, l?utilisateur d�finie sa configuration     C
C      en pr�cisant, en particulier, la position de ces �l�ments:             C
C      - BLOG - "Mesure", "Retrait" ou "Nord"                                 C
C      - CANEL - "Mesure", "Retrait", "Nord" ou "Sud"                         C
C      - BLOC SOURCE - "Source Cf", "Source Am-Be" ou "Source T400"           C
C        Pour ce dernier cas, le BLOC SOURCE sera "Source Cf" avec les        C
C        cellules relatives � cette source pass�es en air (source, capcule,   C
C        tubes, sph�res...)                                                   C
C   3. INCA ins�rera la g�om�trie correspondante (cellules et surfaces) �     C
C      partir d?un fichier externe et supprimera la balise correspondante.    C
C      La suppression de la balise activera les lignes d?exclusion de ces     C
C      �l�ments de la g�om�trie globale du hall CEZANE.                       C
C   4. La pr�sence �ventuelle des "ins�r�s" sur les bancs Van Gogh et T400    C
C      est �galement balis�e.                                                 C
C   5. Balises utilis�s : [BLOG ...]           ... = MESURE/RETRAIT/NORD      C
C                         [CANEL ...]          ... = MESURE/RETRAIT/NORD/SUD  C
C                         [SOURCE ...]         ... = Cf/Am-Be                 C
C                         [INSERE X ...]       ... = VG/T400                  C
C                         [CHARIOT T400 ...]   ... = RECULE/AVANCE            C
C                         [CHARIOT VG ...]     ... = RECULE/AVANCE            C
C   Ainsi ce param�trage sert �galement d?un support � INCA.                  C
C *************************************************************************** C
C /PlageInsertions   100     ; n� pour les nouveaux volumes / surfaces
C --------------------------------------------------------------------------- C
C -----                             VOLUMES                             ----- C
C --------------------------------------------------------------------------- C
998    12   -0.0013  -999 5501 5502 5503 5667 5669  &
                            6949 6953 6957 6958       imp:n=1 imp:p,h,t,d,s=0 $ Monde
999    0                999                           imp:n=0 imp:p,h,t,d,s=0 $ Out of
C **************** C
C ***** HALL ***** C
C **************** C
5501   11   -2.4       -5501 5681 5683 5685 5687 5689 5716 5717 5718 &
                        5701                          imp:n=1 imp:p,h,t,d,s=0 $ Dalle CEZANE
5502   17   -1.2       -5502 5682 5684 5686 5688 5690 &
                        5701 5702 5703 5704 5705 &
                        5706 5707 5708 5709 5710 &
                        5711 5712 5713 5714 5715 &
                        5717 5718 5719 5720 5721 5722 imp:n=1 imp:p,h,t,d,s=0 $ argile sous dalle
5503   15   -2.6989    -5503 5504 5507 5508 5665 5666 imp:n=1 imp:p,h,t,d,s=0 $ bardage ext Al
5504   13   -0.04      -5504 5505 5507 5508 5665 5666 imp:n=1 imp:p,h,t,d,s=0 $ parol�ne
5505   15   -2.6989    -5505 5506 5507 5508 5665 5666 imp:n=1 imp:p,h,t,d,s=0 $ bardage int Al
5506   12   -0.0013  -5665:-5666                    imp:n=1 imp:p,h,t,d,s=0 $ air porte -X et +X
5507   16   -2.54      -5507                          imp:n=1 imp:p,h,t,d,s=0 $ Fenetre -Y
5508   16   -2.54      -5508                          imp:n=1 imp:p,h,t,d,s=0 $ Fenetre +Y
5509   15   -2.6989    -5509 5510                     imp:n=1 imp:p,h,t,d,s=0 $ toit bardage Al
5510   13   -0.04      -5510                          imp:n=1 imp:p,h,t,d,s=0 $ toit parol�ne
5667   15   -2.6989    -5667 5668                     imp:n=1 imp:p,h,t,d,s=0 $ bardage Al porte -X
5668   13   -0.04      -5668                          imp:n=1 imp:p,h,t,d,s=0 $ bardage parol�ne porte -X
5669   15   -2.6989    -5669 5670                     imp:n=1 imp:p,h,t,d,s=0 $ bardage Al porte +X
5670   13   -0.04      -5670                          imp:n=1 imp:p,h,t,d,s=0 $ bardage parol�ne porte +X
C ----- Poutres U 140 -----
5511   14   -7.8212    -5511 5512                     imp:n=1 imp:p,h,t,d,s=0 $ -Y en 160
5512   12   -0.0013  -5512                          imp:n=1 imp:p,h,t,d,s=0 $ -Y en 160
5513   14   -7.8212    -5513 5514                     imp:n=1 imp:p,h,t,d,s=0 $ -Y en 320
5514   12   -0.0013  -5514                          imp:n=1 imp:p,h,t,d,s=0 $ -Y en 320
5515   14   -7.8212    -5515 5516                     imp:n=1 imp:p,h,t,d,s=0 $ -Y en 480
5516   12   -0.0013  -5516                          imp:n=1 imp:p,h,t,d,s=0 $ -Y en 480
5517   14   -7.8212    -5517 5518                     imp:n=1 imp:p,h,t,d,s=0 $ -Y en 640
5518   12   -0.0013  -5518                          imp:n=1 imp:p,h,t,d,s=0 $ -Y en 640
5519   14   -7.8212    -5519 5520                     imp:n=1 imp:p,h,t,d,s=0 $ -Y en 700
5520   12   -0.0013  -5520                          imp:n=1 imp:p,h,t,d,s=0 $ -Y en 700
5521   14   -7.8212    -5521 5522                     imp:n=1 imp:p,h,t,d,s=0 $ -Y au sol
5522   12   -0.0013  -5522                          imp:n=1 imp:p,h,t,d,s=0 $ -Y au sol
c
5523   14   -7.8212    -5523 5524                     imp:n=1 imp:p,h,t,d,s=0 $ +Y en 160
5524   12   -0.0013  -5524                          imp:n=1 imp:p,h,t,d,s=0 $ +Y en 160
5525   14   -7.8212    -5525 5526                     imp:n=1 imp:p,h,t,d,s=0 $ +Y en 320
5526   12   -0.0013  -5526                          imp:n=1 imp:p,h,t,d,s=0 $ +Y en 320
5527   14   -7.8212    -5527 5528                     imp:n=1 imp:p,h,t,d,s=0 $ +Y en 480
5528   12   -0.0013  -5528                          imp:n=1 imp:p,h,t,d,s=0 $ +Y en 480
5529   14   -7.8212    -5529 5530                     imp:n=1 imp:p,h,t,d,s=0 $ +Y en 640
5530   12   -0.0013  -5530                          imp:n=1 imp:p,h,t,d,s=0 $ +Y en 640
5531   14   -7.8212    -5531 5532                     imp:n=1 imp:p,h,t,d,s=0 $ +Y en 700
5532   12   -0.0013  -5532                          imp:n=1 imp:p,h,t,d,s=0 $ +Y en 700
5533   14   -7.8212    -5533 5534                     imp:n=1 imp:p,h,t,d,s=0 $ +Y au sol
5534   12   -0.0013  -5534                          imp:n=1 imp:p,h,t,d,s=0 $ +Y au sol
c
5535   14   -7.8212    -5535 5536 5665                imp:n=1 imp:p,h,t,d,s=0 $ -X en 160
5536   12   -0.0013  -5536      5665                imp:n=1 imp:p,h,t,d,s=0 $ -X en 160
5537   14   -7.8212    -5537 5538 5665                imp:n=1 imp:p,h,t,d,s=0 $ -X en 320
5538   12   -0.0013  -5538      5665                imp:n=1 imp:p,h,t,d,s=0 $ -X en 320
5539   14   -7.8212    -5539 5540                     imp:n=1 imp:p,h,t,d,s=0 $ -X en 480
5540   12   -0.0013  -5540                          imp:n=1 imp:p,h,t,d,s=0 $ -X en 480
5541   14   -7.8212    -5541 5542                     imp:n=1 imp:p,h,t,d,s=0 $ -X en 640
5542   12   -0.0013  -5542                          imp:n=1 imp:p,h,t,d,s=0 $ -X en 640
5543   14   -7.8212    -5543 5544                     imp:n=1 imp:p,h,t,d,s=0 $ -X en 800
5544   12   -0.0013  -5544                          imp:n=1 imp:p,h,t,d,s=0 $ -X en 800
5545   14   -7.8212    -5545 5546 5665                imp:n=1 imp:p,h,t,d,s=0 $ -X au sol
5546   12   -0.0013  -5546      5665                imp:n=1 imp:p,h,t,d,s=0 $ -X au sol
c
5547   14   -7.8212    -5547 5548 5666                imp:n=1 imp:p,h,t,d,s=0 $ +X en 160
5548   12   -0.0013  -5548      5666                imp:n=1 imp:p,h,t,d,s=0 $ +X en 160
5549   14   -7.8212    -5549 5550 5666                imp:n=1 imp:p,h,t,d,s=0 $ +X en 320
5550   12   -0.0013  -5550      5666                imp:n=1 imp:p,h,t,d,s=0 $ +X en 320
5551   14   -7.8212    -5551 5552                     imp:n=1 imp:p,h,t,d,s=0 $ +X en 480
5552   12   -0.0013  -5552                          imp:n=1 imp:p,h,t,d,s=0 $ +X en 480
5553   14   -7.8212    -5553 5554                     imp:n=1 imp:p,h,t,d,s=0 $ +X en 640
5554   12   -0.0013  -5554                          imp:n=1 imp:p,h,t,d,s=0 $ +X en 640
5555   14   -7.8212    -5555 5556                     imp:n=1 imp:p,h,t,d,s=0 $ +X en 800
5556   12   -0.0013  -5556                          imp:n=1 imp:p,h,t,d,s=0 $ +X en 800
5557   14   -7.8212    -5557 5558 5666                imp:n=1 imp:p,h,t,d,s=0 $ +X au sol
5558   12   -0.0013  -5558      5666                imp:n=1 imp:p,h,t,d,s=0 $ +X au sol
C ----- Poutres I 360 -----
5559   14   -7.8212    -5559 5560 5561                imp:n=1 imp:p,h,t,d,s=0 $ -Y_1
5560   12   -0.0013  -5560                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_1
5561   12   -0.0013  -5561                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_1
5562   14   -7.8212    -5562 5563 5564                imp:n=1 imp:p,h,t,d,s=0 $ -Y_2
5563   12   -0.0013  -5563                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_2
5564   12   -0.0013  -5564                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_2
5565   14   -7.8212    -5565 5566 5567                imp:n=1 imp:p,h,t,d,s=0 $ -Y_3
5566   12   -0.0013  -5566                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_3
5567   12   -0.0013  -5567                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_3
5568   14   -7.8212    -5568 5569 5570                imp:n=1 imp:p,h,t,d,s=0 $ -Y_4
5569   12   -0.0013  -5569                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_4
5570   12   -0.0013  -5570                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_4
5571   14   -7.8212    -5571 5572 5573                imp:n=1 imp:p,h,t,d,s=0 $ -Y_5
5572   12   -0.0013  -5572                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_5
5573   12   -0.0013  -5573                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_5
5574   14   -7.8212    -5574 5575 5576                imp:n=1 imp:p,h,t,d,s=0 $ -Y_6
5575   12   -0.0013  -5575                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_6
5576   12   -0.0013  -5576                          imp:n=1 imp:p,h,t,d,s=0 $ -Y_6
c
5577   14   -7.8212    -5577 5578 5579                imp:n=1 imp:p,h,t,d,s=0 $ +Y_1
5578   12   -0.0013  -5578                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_1
5579   12   -0.0013  -5579                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_1
5580   14   -7.8212    -5580 5581 5582                imp:n=1 imp:p,h,t,d,s=0 $ +Y_2
5581   12   -0.0013  -5581                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_2
5582   12   -0.0013  -5582                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_2
5583   14   -7.8212    -5583 5584 5585                imp:n=1 imp:p,h,t,d,s=0 $ +Y_3
5584   12   -0.0013  -5584                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_3
5585   12   -0.0013  -5585                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_3
5586   14   -7.8212    -5586 5587 5588                imp:n=1 imp:p,h,t,d,s=0 $ +Y_4
5587   12   -0.0013  -5587                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_4
5588   12   -0.0013  -5588                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_4
5589   14   -7.8212    -5589 5590 5591                imp:n=1 imp:p,h,t,d,s=0 $ +Y_5
5590   12   -0.0013  -5590                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_5
5591   12   -0.0013  -5591                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_5
5592   14   -7.8212    -5592 5593 5594                imp:n=1 imp:p,h,t,d,s=0 $ +Y_6
5593   12   -0.0013  -5593                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_6
5594   12   -0.0013  -5594                          imp:n=1 imp:p,h,t,d,s=0 $ +Y_6
c
5595   14   -7.8212    -5595 5596 5597                imp:n=1 imp:p,h,t,d,s=0 $ +Z_1
5596   12   -0.0013  -5596                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_1
5597   12   -0.0013  -5597                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_1
5598   14   -7.8212    -5598 5599 5600                imp:n=1 imp:p,h,t,d,s=0 $ +Z_2
5599   12   -0.0013  -5599                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_2
5600   12   -0.0013  -5600                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_2
5601   14   -7.8212    -5601 5602 5603                imp:n=1 imp:p,h,t,d,s=0 $ +Z_3
5602   12   -0.0013  -5602                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_3
5603   12   -0.0013  -5603                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_3
5604   14   -7.8212    -5604 5605 5606                imp:n=1 imp:p,h,t,d,s=0 $ +Z_4
5605   12   -0.0013  -5605                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_4
5606   12   -0.0013  -5606                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_4
5607   14   -7.8212    -5607 5608 5609                imp:n=1 imp:p,h,t,d,s=0 $ +Z_5
5608   12   -0.0013  -5608                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_5
5609   12   -0.0013  -5609                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_5
5610   14   -7.8212    -5610 5611 5612                imp:n=1 imp:p,h,t,d,s=0 $ +Z_6
5611   12   -0.0013  -5611                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_6
5612   12   -0.0013  -5612                          imp:n=1 imp:p,h,t,d,s=0 $ +Z_6
C ----- Poutres I 300 -----
5613   14   -7.8212    -5613 5614 5615                imp:n=1 imp:p,h,t,d,s=0 $ -X_1
5614   12   -0.0013  -5614                          imp:n=1 imp:p,h,t,d,s=0 $ -X_1
5615   12   -0.0013  -5615                          imp:n=1 imp:p,h,t,d,s=0 $ -X_1
5616   14   -7.8212    -5616 5617 5618                imp:n=1 imp:p,h,t,d,s=0 $ -X_2
5617   12   -0.0013  -5617                          imp:n=1 imp:p,h,t,d,s=0 $ -X_2
5618   12   -0.0013  -5618                          imp:n=1 imp:p,h,t,d,s=0 $ -X_2
5619   14   -7.8212    -5619 5620 5621                imp:n=1 imp:p,h,t,d,s=0 $ -X_3
5620   12   -0.0013  -5620                          imp:n=1 imp:p,h,t,d,s=0 $ -X_3
5621   12   -0.0013  -5621                          imp:n=1 imp:p,h,t,d,s=0 $ -X_3
5622   14   -7.8212    -5622 5623 5624                imp:n=1 imp:p,h,t,d,s=0 $ +X_1
5623   12   -0.0013  -5623                          imp:n=1 imp:p,h,t,d,s=0 $ +X_1
5624   12   -0.0013  -5624                          imp:n=1 imp:p,h,t,d,s=0 $ +X_1
5625   14   -7.8212    -5625 5626 5627                imp:n=1 imp:p,h,t,d,s=0 $ +X_2
5626   12   -0.0013  -5626                          imp:n=1 imp:p,h,t,d,s=0 $ +X_2
5627   12   -0.0013  -5627                          imp:n=1 imp:p,h,t,d,s=0 $ +X_2
5628   14   -7.8212    -5628 5629 5630                imp:n=1 imp:p,h,t,d,s=0 $ +X_3
5629   12   -0.0013  -5629                          imp:n=1 imp:p,h,t,d,s=0 $ +X_3
5630   12   -0.0013  -5630                          imp:n=1 imp:p,h,t,d,s=0 $ +X_3
C ----- Poutres U 300 (portes) -----
5631   14   -7.8212    -5631 5632                     imp:n=1 imp:p,h,t,d,s=0 $ -X porte
5632   12   -0.0013  -5632                          imp:n=1 imp:p,h,t,d,s=0 $ -X porte
5633   14   -7.8212    -5633 5634                     imp:n=1 imp:p,h,t,d,s=0 $ +X porte
5634   12   -0.0013  -5634                          imp:n=1 imp:p,h,t,d,s=0 $ +X porte
C ----- Poutres I 140 (toit) -----
5635   14   -7.8212    -5635 5636 5637                imp:n=1 imp:p,h,t,d,s=0 $ -X_1
5636   12   -0.0013  -5636                          imp:n=1 imp:p,h,t,d,s=0 $ -X_1
5637   12   -0.0013  -5637                          imp:n=1 imp:p,h,t,d,s=0 $ -X_1
5638   14   -7.8212    -5638 5639 5640                imp:n=1 imp:p,h,t,d,s=0 $ -X_2
5639   12   -0.0013  -5639                          imp:n=1 imp:p,h,t,d,s=0 $ -X_2
5640   12   -0.0013  -5640                          imp:n=1 imp:p,h,t,d,s=0 $ -X_2
5641   14   -7.8212    -5641 5642 5643                imp:n=1 imp:p,h,t,d,s=0 $ -X_3
5642   12   -0.0013  -5642                          imp:n=1 imp:p,h,t,d,s=0 $ -X_3
5643   12   -0.0013  -5643                          imp:n=1 imp:p,h,t,d,s=0 $ -X_3
5644   14   -7.8212    -5644 5645 5646                imp:n=1 imp:p,h,t,d,s=0 $ +X_4
5645   12   -0.0013  -5645                          imp:n=1 imp:p,h,t,d,s=0 $ +X_4
5646   12   -0.0013  -5646                          imp:n=1 imp:p,h,t,d,s=0 $ +X_4
5647   14   -7.8212    -5647 5648 5649                imp:n=1 imp:p,h,t,d,s=0 $ +X_5
5648   12   -0.0013  -5648                          imp:n=1 imp:p,h,t,d,s=0 $ +X_5
5649   12   -0.0013  -5649                          imp:n=1 imp:p,h,t,d,s=0 $ +X_5
5650   14   -7.8212    -5650 5651 5652                imp:n=1 imp:p,h,t,d,s=0 $ +X_6
5651   12   -0.0013  -5651                          imp:n=1 imp:p,h,t,d,s=0 $ +X_6
5652   12   -0.0013  -5652                          imp:n=1 imp:p,h,t,d,s=0 $ +X_6
C ----- Rails -----
5653   14   -7.8212    -5653:-5654:-5655              imp:n=1 imp:p,h,t,d,s=0 $ -Y
5656   14   -7.8212    -5656:-5657:-5658              imp:n=1 imp:p,h,t,d,s=0 $ +Y
C ----- Pont Roulant -----
5661   14   -7.8212    -5661 5662                     imp:n=1 imp:p,h,t,d,s=0 $ Poutre_1
5662   12   -0.0013  -5662                          imp:n=1 imp:p,h,t,d,s=0 $ Poutre_1
5663   14   -7.8212    -5663 5664                     imp:n=1 imp:p,h,t,d,s=0 $ Poutre_2
5664   12   -0.0013  -5664                          imp:n=1 imp:p,h,t,d,s=0 $ Poutre_2
c ----- Caniveaux -----
5681   12  -0.0013  -5681 5691 5692 5694 5696 5698 5700 imp:n=1 imp:p,h,t,d,s=0 $ air Caniveau -X
5682   11   -2.4       -5682 5681 5683 5685 5687 5689 imp:n=1 imp:p,h,t,d,s=0 $ Caniveau -X
5683   12   -0.0013  -5683 5693 5694                imp:n=1 imp:p,h,t,d,s=0 $ air Caniveau Y1
5684   11   -2.4       -5684 5683                     imp:n=1 imp:p,h,t,d,s=0 $ Caniveau Y1
5685   12   -0.0013  -5685 5695 5696                imp:n=1 imp:p,h,t,d,s=0 $ air Caniveau Y2
5686   11   -2.4       -5686 5685                     imp:n=1 imp:p,h,t,d,s=0 $ Caniveau Y2
5687   12   -0.0013  -5687 5697 5698                imp:n=1 imp:p,h,t,d,s=0 $ air Caniveau Y3
5688   11   -2.4       -5688 5687                     imp:n=1 imp:p,h,t,d,s=0 $ Caniveau Y3
5689   12   -0.0013  -5689 5699 5700                imp:n=1 imp:p,h,t,d,s=0 $ air Caniveau Y4
5690   11   -2.4       -5690 5689                     imp:n=1 imp:p,h,t,d,s=0 $ Caniveau Y4
c ----- plaques acier et cables -----
5691   14   -7.8212    -5691                          imp:n=1 imp:p,h,t,d,s=0 $ Plaque -X
5692   41   -1.734     -5692                          imp:n=1 imp:p,h,t,d,s=0 $ Cables 10x10x -X
5693   14   -7.8212    -5693                          imp:n=1 imp:p,h,t,d,s=0 $ Plaque Y1
5694   41   -1.734     -5694                          imp:n=1 imp:p,h,t,d,s=0 $ Cables 10x10  Y1
5695   14   -7.8212    -5695                          imp:n=1 imp:p,h,t,d,s=0 $ Plaque Y2
5696   41   -1.734     -5696                          imp:n=1 imp:p,h,t,d,s=0 $ Cables 10x10  Y2
5697   14   -7.8212    -5697                          imp:n=1 imp:p,h,t,d,s=0 $ Plaque Y3
5698   41   -1.734     -5698                          imp:n=1 imp:p,h,t,d,s=0 $ Cables 10x10  Y3
5699   14   -7.8212    -5699                          imp:n=1 imp:p,h,t,d,s=0 $ Plaque Y4
5700   41   -1.734     -5700                          imp:n=1 imp:p,h,t,d,s=0 $ Cables 10x10  Y4
c ----- Escalier -----
5701   11   -2.4       -5701                          imp:n=1 imp:p,h,t,d,s=0 $ marche 01
5702   11   -2.4       -5702                          imp:n=1 imp:p,h,t,d,s=0 $ marche 02
5703   11   -2.4       -5703                          imp:n=1 imp:p,h,t,d,s=0 $ marche 03
5704   11   -2.4       -5704                          imp:n=1 imp:p,h,t,d,s=0 $ marche 04
5705   11   -2.4       -5705                          imp:n=1 imp:p,h,t,d,s=0 $ marche 05
5706   11   -2.4       -5706                          imp:n=1 imp:p,h,t,d,s=0 $ marche 06
5707   11   -2.4       -5707                          imp:n=1 imp:p,h,t,d,s=0 $ marche 07
5708   11   -2.4       -5708                          imp:n=1 imp:p,h,t,d,s=0 $ marche 08
5709   11   -2.4       -5709                          imp:n=1 imp:p,h,t,d,s=0 $ marche 09
5710   11   -2.4       -5710                          imp:n=1 imp:p,h,t,d,s=0 $ marche 10
5711   11   -2.4       -5711                          imp:n=1 imp:p,h,t,d,s=0 $ marche 11
5712   11   -2.4       -5712                          imp:n=1 imp:p,h,t,d,s=0 $ marche 12
5713   11   -2.4       -5713                          imp:n=1 imp:p,h,t,d,s=0 $ marche 13
5714   11   -2.4       -5714                          imp:n=1 imp:p,h,t,d,s=0 $ marche 14
5715   11   -2.4       -5715                          imp:n=1 imp:p,h,t,d,s=0 $ marche 15
5716   12   -0.0013  (-5716:-5717:-5718:-5719:-5720:-5721:-5722) & 
                         5702 5703 5705 5706 5709 5711 5712 5714 5715 &
                                                      imp:n=1 imp:p,h,t,d,s=0 $ air escalier
c ----- Garde Corps escalier -----
5723   14   -7.8212    -5723 5724                     imp:n=1 imp:p,h,t,d,s=0 $ poteau -X-Y 
5724   12   -0.0013  -5724                          imp:n=1 imp:p,h,t,d,s=0 $ air poteau -X-Y
5725   14   -7.8212    -5725 5726                     imp:n=1 imp:p,h,t,d,s=0 $ poteau +X-Y
5726   12   -0.0013  -5726                          imp:n=1 imp:p,h,t,d,s=0 $ air poteau +X-Y
5727   14   -7.8212    -5727 5728                     imp:n=1 imp:p,h,t,d,s=0 $ poteau -X+Y
5728   12   -0.0013  -5728                          imp:n=1 imp:p,h,t,d,s=0 $ air poteau -X+Y
5729   14   -7.8212    -5729 5730                     imp:n=1 imp:p,h,t,d,s=0 $ poteau +X+Y
5730   12   -0.0013  -5730                          imp:n=1 imp:p,h,t,d,s=0 $ air poteau +X+Y
5731   14   -7.8212    -5731 5732                     imp:n=1 imp:p,h,t,d,s=0 $ poteaux -Y
5732   12   -0.0013  -5732                          imp:n=1 imp:p,h,t,d,s=0 $
5733   14   -7.8212    -5733 5734                     imp:n=1 imp:p,h,t,d,s=0 $
5734   12   -0.0013  -5734                          imp:n=1 imp:p,h,t,d,s=0 $
5735   14   -7.8212    -5735 5736                     imp:n=1 imp:p,h,t,d,s=0 $ poteau +Y
5736   12   -0.0013  -5736                          imp:n=1 imp:p,h,t,d,s=0 $ 
5737   14   -7.8212    -5737 5738                     imp:n=1 imp:p,h,t,d,s=0 $ 
5738   12   -0.0013  -5738                          imp:n=1 imp:p,h,t,d,s=0 $
5739   14   -7.8212    -5739 5740 5731 5733           imp:n=1 imp:p,h,t,d,s=0 $ barre -Y
5740   12   -0.0013  -5740      5731 5733           imp:n=1 imp:p,h,t,d,s=0 $
5741   14   -7.8212    -5741 5742 5735 5737           imp:n=1 imp:p,h,t,d,s=0 $ barre +Y
5742   12   -0.0013  -5742      5735 5737           imp:n=1 imp:p,h,t,d,s=0 $
5743   14   -7.8212    -5743 5744                     imp:n=1 imp:p,h,t,d,s=0 $ barre -X
5744   12   -0.0013  -5744                          imp:n=1 imp:p,h,t,d,s=0 $
5745   14   -7.8212    -5745 5746                     imp:n=1 imp:p,h,t,d,s=0 $ barres +Z
5746   12   -0.0013  -5746                          imp:n=1 imp:p,h,t,d,s=0 $
5747   14   -7.8212    -5747 5748                     imp:n=1 imp:p,h,t,d,s=0 $
5748   12   -0.0013  -5748                          imp:n=1 imp:p,h,t,d,s=0 $
5749   14   -7.8212    -5749 5750                     imp:n=1 imp:p,h,t,d,s=0 $
5750   12   -0.0013  -5750                          imp:n=1 imp:p,h,t,d,s=0 $
c ----- Encommbrement -----
6901   38   -1.2       -6901                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 1 Armoires elec.
6902   38   -1.4844    -6902                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 2 Compresseur jaune
6903   23   -0.3493    -6903                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 2 Ballon
6904   38   -1.2       -6904                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 3 Armoire elec.
6905   38   -1.4844    -6905                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 3 mini-compresseur
6906   38   -1.4844    -6906                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 3 Compresseur bleu
6907   23   -0.3493    -6907                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 3 Ballon
6908   39   -0.0694    -6908                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 4 Armore grise vide
6909   39   -0.0694    -6909                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 4 Deux Armores grises
6910   38   -1.2       -6910                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 4 Armoir elec.
6911   38   -1.2       -6911                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 4 Deux Armores elec
6912   38   -1.2       -6912                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 4 Armoir elec.
6913   38   -1.2       -6913:-6914                    imp:n=1 imp:p,h,t,d,s=0 $ Bloc 5 Armoir elec. T400
6915   38   -1.2       -6915                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 6 Armoires elec. Van Gogh
6916   38   -1.2       -6916                          imp:n=1 imp:p,h,t,d,s=0
6917   38   -1.2       -6917                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 7 Armoires elec. sous Van Gogh
6918   38   -1.2       -6918                          imp:n=1 imp:p,h,t,d,s=0
6919   38   -1.2       -6919                          imp:n=1 imp:p,h,t,d,s=0 $ Bloc 8 Armoires elec. sous Van Gogh
6920   38   -1.2       -6920                          imp:n=1 imp:p,h,t,d,s=0
6921   38   -1.2       -6921                          imp:n=1 imp:p,h,t,d,s=0
6922   11   -2.4       -6922:-6923:-6924              imp:n=1 imp:p,h,t,d,s=0 $ Muret local source
6925   39   -0.6250    -6925                          imp:n=1 imp:p,h,t,d,s=0 $ Armoire 1 M=500 kg
6926   39   -0.6250    -6926                          imp:n=1 imp:p,h,t,d,s=0 $ Armoire 2 m�me densit�, M=262.5 kg
6927   15   -2.6989    -6927 6928 5511 5521 5574 5575 &
                                 5622 5666 5547 5557  imp:n=1 imp:p,h,t,d,s=0 $ Local B�G
6928   55   -0.9       -6928 6929 5511 5521 5574 5575 &
                                 5622 5666 5547 5557  imp:n=1 imp:p,h,t,d,s=0 
6929   15   -2.6989    -6929 6930 5511 5521 5574 5575 &
                                 5622 5666 5547 5557  imp:n=1 imp:p,h,t,d,s=0 
6930   12   -0.0013  -6930      5511 5521 5574 5575 &
                                 5622 5666 5547 5557  imp:n=1 imp:p,h,t,d,s=0 
6931   29   -0.0949    -6931                          imp:n=1 imp:p,h,t,d,s=0 $ Ventilation devant local BaG
c ----- Ballon HF6 -----
6932   14   -7.8212    -6932 6933                     imp:n=1 imp:p,h,t,d,s=0 $ Ballon HF6
6933   64   -0.03597   -6933                          imp:n=1 imp:p,h,t,d,s=0
c ----- Support en T -----
6934   43   -1.2013    -6934:-6935                    imp:n=1 imp:p,h,t,d,s=0 $ Pieds
6936   14   -7.8212    -6936 6937 6938                imp:n=1 imp:p,h,t,d,s=0 $ Tube vertical
6937   12   -0.0013  -6937      6938                imp:n=1 imp:p,h,t,d,s=0
6938   14   -7.8212    -6938 6939 6940                imp:n=1 imp:p,h,t,d,s=0 $ Gros tube horizontal
6939   12   -0.0013  -6939      6940                imp:n=1 imp:p,h,t,d,s=0
6940   14   -7.8212    -6940 6941                     imp:n=1 imp:p,h,t,d,s=0 $ Petit tube horizontal
6941   12   -0.0013  -6941                          imp:n=1 imp:p,h,t,d,s=0
6942   55   -0.9000    -6942 6943 6940                imp:n=1 imp:p,h,t,d,s=0 $ Soufflet
6943   12   -0.0013  -6943      6940                imp:n=1 imp:p,h,t,d,s=0
C ************************************************** C
C ***** Air p�riph�rique hors zones de travail ***** C
C ************************************************** C
6944   12   -0.0013  -6944 6945 6946 6947           & $ Air hors zone travail
                        5665 5666 5509                & $ Toit et air portes
                        5511 5513 5515 5517 5519 5521 & $ Poutres U 140
                        5523 5525 5527 5529 5531 5533 &
                        5535 5537 5539 5541 5543 5545 &
                        5547 5549 5551 5553 5555 5557 &
                        5559 5562 5565 5568 5571 5574 & $ Poutres I 360
                        5577 5580 5583 5586 5589 5592 &
                        5595 5598 5601 5604 5607 5610 &
                        5613 5616 5619 5622 5625 5628 & $ Poutres I 300
                        5631 5633 5507 5508           & $ Poutres U 300 portes, fenetres
                        5635 5638 5641 5644 5647 5650 & $ Poutres I 140 toit
              5653 5654 5655 5656 5657 5658 5661 5663 & $ Rails et pont roulant
                   5723 5725 5727 5729 5731 5733 5735 & $ Garde-corps escalier d'acc�s
                   5737 5739 5741 5743 5745 5747 5749 &
                   6901 6902 6903 6904 6905 6906 6907 & $ Encombrement
                   6908 6909 6910 6911 6912 6922 6923 &
                   6924 6925 6926 6927 6931 6932 5981 &
                                                      imp:n=1 imp:p,h,t,d,s=0 $ Air hors zone travail
C ******************************************************** C
C ***** Air zone de travail VAN GOGH (Z = 0 - 203.5) ***** C
C ******************************************************** C
6945  12 -0.0013  -6945 5761 5786 5796 5797 5798 &
    5801 5802 5803 5806 5807 5808 5810 5812 5814 5816 5818 &
    5820 5822 5823 5824 5827 5828 5829 5834 5835 5836 5838 &
    5839 5840 5842 5843 5844 5846 5847 5848 5850 5851 5852 &
    5854 5855 5856 5858 5859 5860 5861 5863 5864 5865 6001 &
    6003 6005 6006 6007 6008 6010 6011 6012 6013 6016 6017 &
    6018 6019 6020 6021 6022 6033 6038 6043 6044 6045 6046 &
    6047 6048 6049 6050 6062 6063 6064 6065 6066 6067 6068 &
    6069 6070 6071 6072 6073 6074 6075 6076 6077 6078 6079 &
    6080 6081 6082 6083 6084 6085 6086 6090 6091 6092 6093 &
    6094 6095 6097 6098 6099 6100 6101 6102 6104 6105 6106 &
    6107 6108 6109 6111 6112 6113 6114 6115 6116 6118 6119 &
    6120 6121 6122 6123 6124 6125 6126 6701 6705 6706 6707 &
    6757 6758 6759 6915 6916 6917 6918 6919 6920 6921 5981 &
    7021 7070 7120 7121 7066 7067 7068 7069 7064 7065 7062 &
    imp:n=1 imp:p,h,t,d,s=0 $ Air zone travail VAN GOGH Z=0 - 203.5
C ************************************************************ C
C ***** Air zone de travail VAN GOGH (Z = 203.5 - 500.0) ***** C
C ************************************************************ C
6946  12 -0.0013  -6946 5751 5753 5755 5757 5759 &
    5763 5765 5767 5769 5771 5773 5775 5781 5782 5783 5784 &
    5785 5787 5788 5789 5790 5791 5792 5866 5867 5868 5869 &
    5870 5871 5872 5873 5874 5875 6010 6011 6012 6009 6014 &
    6015 6031 6013 6020 6033 6038 6126 6130 6131 6132 6133 &
    6135 6136 6137 6138 6139 6140 6141 6142 6143 5981 6701 &
    6706 6707 6709 6710 6711 6712 6713 6714 6715 6716 6717 &
    6719 6721 6722 6723 6724 6725 6726 6727 6728 6729 6730 &
    6731 6732 6733 6736 7059 7060 7061 7062 7080 7053 7055 &
    7056 #100 #101 #102 #103 #104 #105 #106 #107 #108 #109 #110 #111 &
    #112 #113 #114 #115 #116 #117 #118 #119 #120 #121 #122 #123 #124 #130 &
    (6734:6735) 6736 (6738:6739) #6740 6744 6745 &
    6746 (6747:6748) 6749 6750 6751 6752 6753 6754 6755 &
    6756 6757 6758 6759 #6760 imp:n=1 imp:p,h,t,d,s=0 $ Air zone travail VAN GOGH Z=203.5 - 500
C ************************************ C
C ***** Air zone de travail T400 ***** C
C ************************************ C
6947  12 -0.0013  -6947 6948 6934 6935 6936 6938 &
    6940 6942 6240 6411 6412 6413 6414 6169 6170 6171 6172 &
    6173 6174 6175 6176 6177 6178 6179 6180 6181 6182 6183 &
    6184 6185 6186 6187 6188 6189 6190 6191 6192 6193 6194 &
    6195 6196 6197 6198 6199 6200 6201 6202 6203 6204 6205 &
    6206 6107 6208 6209 6210 6211 6212 6213 6214 6215 6242 &
    6243 6244 6245 6246 6247 6248 6249 6250 6251 6252 6253 &
    6256 6259 6262 6265 6268 6269 6301 6307 6308 6310 6311 &
    6314 6315 6316 6317 6318 6319 6320 6321 6322 6323 6325 &
    6327 6381 6383 6384 6385 6386 6389 6390 6391 6393 6395 &
    6397 6398 6400 6402 6404 6405 6406 6407 6421 6422 #6330 &
    #6331 #6332 #6333 #6334 #6350 #6351 #6352 #6353 #6354 &
    #6370 #6371 #6372 #6373 #6374 #6418 6913 6914 6645 &
    6578 imp:n=1 imp:p,h,t,d,s=0 $ Air zone travail T400
C ******************************************* C
C ***** Air zone de travail T400 - Banc ***** C
C ******************************************* C
6948  12 -0.0013  -6948 #6418 6422 6327 6325 6323 &
    6314 6315 6316 6317 6311 6318 6319 6320 6321 6322 6301 &
    6307 6308 6310 6236 6237 6238 6239 6224 6225 6226 6227 &
    6228 6229 6230 6231 6232 6234 6601 6602 6603 6605 6606 &
    6607 6608 6609 6610 6611 6612 6613 6614 6615 6616 6617 &
    6618 6619 #6620 #6621 #6622 #6625 #6629 #6634 6630 &
    6631 6632 6633 6635 6636 6637 6638 6450 6488 6489 6490 &
    imp:n=1 imp:p,h,t,d,s=0 $ Air zone travail T400 - Banc
C ************************* C
C ***** Local D�chets ***** C
C ************************* C
6949   15   -2.6989    -6949 6950                     imp:n=1 imp:p,h,t,d,s=0 $ Bardage ext couloir
6950   55   -0.9       -6950 6951                     imp:n=1 imp:p,h,t,d,s=0 $ Polypropyl�ne couloir
6951   15   -2.6989    -6951 6952                     imp:n=1 imp:p,h,t,d,s=0 $ Bardage int couloir
6952   12   -0.0013  -6952                          imp:n=1 imp:p,h,t,d,s=0 $ Air couloir
6953   15   -2.6989    -6953 6954                     imp:n=1 imp:p,h,t,d,s=0 $ Bardage ext local
6954   55   -0.9       -6954 6955                     imp:n=1 imp:p,h,t,d,s=0 $ Polypropyl�ne local
6955   15   -2.6989    -6955 6956                     imp:n=1 imp:p,h,t,d,s=0 $ Bardage int local
6956   12   -0.0013  -6956                          imp:n=1 imp:p,h,t,d,s=0 $ Air local
6957   11   -2.4       -6957                          imp:n=1 imp:p,h,t,d,s=0 $ Dalle
6958   17   -1.2       -6958                          imp:n=1 imp:p,h,t,d,s=0 $ Argile
C ******************************* C
C ***** PLATEFORME VAN GOGH ***** C
C ******************************* C
c ----- Structure -----
5751   43   -1.8962    -5751 5752                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure A
5752   12   -0.0013  -5752 5795 5796 5797 5799 5800 &
                        5801 5802 5804 5805 5806 5807 imp:n=1 imp:p,h,t,d,s=0
5753   43   -1.8962    -5753 5754                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure B
5754   12   -0.0013  -5754                          imp:n=1 imp:p,h,t,d,s=0
5755   43   -1.8962    -5755 5756                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure C
5756   12   -0.0013  -5756 5809 5810 5811 5812 5813 &
                             5814 5815 5816           imp:n=1 imp:p,h,t,d,s=0
5757   43   -1.8962    -5757 5758                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure D
5758   12   -0.0013  -5758 5817 5818 5819 5820      imp:n=1 imp:p,h,t,d,s=0
5759   43   -1.8962    -5759 5760                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure E
5760   12   -0.0013  -5760 5821 5822 5823 5825 5826 &
                             5827 5828                imp:n=1 imp:p,h,t,d,s=0
5761   43   -1.8962    -5761 5762                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure F
5762   12   -0.0013  -5762 5830 5831 5832           imp:n=1 imp:p,h,t,d,s=0
5763   43   -1.8962    -5763 5764                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure G
5764   12   -0.0013  -5764 5833 5834 5835 5837 5838 &
                             5839                     imp:n=1 imp:p,h,t,d,s=0
5765   43   -1.8962    -5765 5766                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure H
5766   12   -0.0013  -5766 5841 5842 5843 5845 5846 &
                             5847                     imp:n=1 imp:p,h,t,d,s=0
5767   43   -1.8962    -5767 5768                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure I
5768   12   -0.0013  -5768                          imp:n=1 imp:p,h,t,d,s=0
5769   43   -1.8962    -5769 5770                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure J
5770   12   -0.0013  -5770 5849 5850 5851 5853 5854 &
                             5855                     imp:n=1 imp:p,h,t,d,s=0
5771   43   -1.8962    -5771 5772                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure K
5772   12   -0.0013  -5772 5857 5858 5859           imp:n=1 imp:p,h,t,d,s=0
5773   43   -1.8962    -5773 5774                     imp:n=1 imp:p,h,t,d,s=0 $ Sructure L
5774   12   -0.0013  -5774 5861 5862 5863 5864 5775 imp:n=1 imp:p,h,t,d,s=0
5775   43   -1.8962    -5775 5776                     imp:n=1 imp:p,h,t,d,s=0 $ Structure -X suppl.
5776   12   -0.0013  -5776                          imp:n=1 imp:p,h,t,d,s=0
c ----- Caillebotis -----
5781   39   -0.924     -5781                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis A
5782   39   -0.924     -5782                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis B
5783   39   -0.924     -5783                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis C
5784   39   -0.924     -5784                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis D
5785   39   -0.924     -5785                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis E
5786   39   -0.924     -5786                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis F
5787   39   -0.924     -5787                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis G
5788   39   -0.924     -5788                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis H
5789   39   -0.924     -5789                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis I
5790   39   -0.924     -5790                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis J
5791   39   -0.924     -5791                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis K
5792   39   -0.924     -5792                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis L
c ----- Renforts structure + pieds -----
5795   43   -2.1614    -5795                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P5_A
5796   43   -2.1614    -5796                          imp:n=1 imp:p,h,t,d,s=0 
5797   43   -2.1614    -5797                          imp:n=1 imp:p,h,t,d,s=0 
5798   43   -2.1614    -5798                          imp:n=1 imp:p,h,t,d,s=0 
5799   43   -1.8962    -5799                          imp:n=1 imp:p,h,t,d,s=0 $ Renfort A
5800   43   -2.3491    -5800                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P6_A
5801   43   -2.3491    -5801                          imp:n=1 imp:p,h,t,d,s=0 
5802   43   -2.3491    -5802                          imp:n=1 imp:p,h,t,d,s=0 
5803   43   -2.3491    -5803                          imp:n=1 imp:p,h,t,d,s=0 
5804   43   -1.8962    -5804                          imp:n=1 imp:p,h,t,d,s=0 $ Renfort A
5805   43   -2.1614    -5805                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P7_A
5806   43   -2.1614    -5806                          imp:n=1 imp:p,h,t,d,s=0 
5807   43   -2.1614    -5807                          imp:n=1 imp:p,h,t,d,s=0 
5808   43   -2.1614    -5808                          imp:n=1 imp:p,h,t,d,s=0
5809   43   -1.8484    -5809                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P2_C
5810   43   -1.8484    -5810                          imp:n=1 imp:p,h,t,d,s=0 
5811   43   -1.8484    -5811                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P1_C
5812   43   -1.9869    -5812                          imp:n=1 imp:p,h,t,d,s=0 
5813   43   -1.9869    -5813                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P1_C
5814   43   -1.9869    -5814                          imp:n=1 imp:p,h,t,d,s=0 
5815   43   -1.9869    -5815                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P1_C
5816   43   -1.9869    -5816                          imp:n=1 imp:p,h,t,d,s=0 
5817   43   -1.9869    -5817                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P1_D
5818   43   -1.9869    -5818                          imp:n=1 imp:p,h,t,d,s=0 
5819   43   -1.9869    -5819                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P1_D
5820   43   -1.9869    -5820                          imp:n=1 imp:p,h,t,d,s=0
5821   43   -2.0796    -5821                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P3_E
5822   43   -2.0796    -5822                          imp:n=1 imp:p,h,t,d,s=0
5823   43   -2.0796    -5823                          imp:n=1 imp:p,h,t,d,s=0 
5824   43   -2.0796    -5824                          imp:n=1 imp:p,h,t,d,s=0 
5825   43   -1.8962    -5825                          imp:n=1 imp:p,h,t,d,s=0 $ Renfort E
5826   43   -2.0796    -5826                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P4_E
5827   43   -2.0796    -5827                          imp:n=1 imp:p,h,t,d,s=0 
5828   43   -2.0796    -5828                          imp:n=1 imp:p,h,t,d,s=0 
5829   43   -2.0796    -5829                          imp:n=1 imp:p,h,t,d,s=0 
5830   43   -1.8962    -5830                          imp:n=1 imp:p,h,t,d,s=0 $ Renfort F
5831   43   -1.8962    -5831                          imp:n=1 imp:p,h,t,d,s=0 
5832   43   -1.8962    -5832                          imp:n=1 imp:p,h,t,d,s=0 
5833   43   -2.0796    -5833                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P4_G
5834   43   -2.0796    -5834                          imp:n=1 imp:p,h,t,d,s=0 
5835   43   -2.0796    -5835                          imp:n=1 imp:p,h,t,d,s=0 
5836   43   -2.0796    -5836                          imp:n=1 imp:p,h,t,d,s=0 
5837   43   -2.0796    -5837                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds P3_G
5838   43   -2.0796    -5838                          imp:n=1 imp:p,h,t,d,s=0 
5839   43   -2.0796    -5839                          imp:n=1 imp:p,h,t,d,s=0 
5840   43   -2.0796    -5840                          imp:n=1 imp:p,h,t,d,s=0 
5841   43   -2.1614    -5841                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds PX_H
5842   43   -2.1614    -5842                          imp:n=1 imp:p,h,t,d,s=0 
5843   43   -2.1614    -5843                          imp:n=1 imp:p,h,t,d,s=0 
5844   43   -2.1614    -5844                          imp:n=1 imp:p,h,t,d,s=0 
5845   43   -2.1614    -5845                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds PX_H
5846   43   -2.1614    -5846                          imp:n=1 imp:p,h,t,d,s=0 
5847   43   -2.1614    -5847                          imp:n=1 imp:p,h,t,d,s=0 
5848   43   -2.1614    -5848                          imp:n=1 imp:p,h,t,d,s=0 
5849   43   -2.1614    -5849                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds PX_J
5850   43   -2.1614    -5850                          imp:n=1 imp:p,h,t,d,s=0 
5851   43   -2.1614    -5851                          imp:n=1 imp:p,h,t,d,s=0 
5852   43   -2.1614    -5852                          imp:n=1 imp:p,h,t,d,s=0 
5853   43   -2.1614    -5853                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds PX_J
5854   43   -2.1614    -5854                          imp:n=1 imp:p,h,t,d,s=0 
5855   43   -2.1614    -5855                          imp:n=1 imp:p,h,t,d,s=0 
5856   43   -2.1614    -5856                          imp:n=1 imp:p,h,t,d,s=0 
5857   43   -2.1614    -5857                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds PX_K
5858   43   -2.1614    -5858                          imp:n=1 imp:p,h,t,d,s=0 
5859   43   -2.1614    -5859                          imp:n=1 imp:p,h,t,d,s=0 
5860   43   -2.1614    -5860                          imp:n=1 imp:p,h,t,d,s=0 
5861   43   -2.1614    -5861                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds PX_L
5862   43   -2.1614    -5862                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds PX_L
5863   43   -2.1614    -5863                          imp:n=1 imp:p,h,t,d,s=0 
5864   43   -2.1614    -5864                          imp:n=1 imp:p,h,t,d,s=0 
5865   43   -2.1614    -5865                          imp:n=1 imp:p,h,t,d,s=0
c ----- Garde-corps -----
5866   44   -2.7       -5866                          imp:n=1 imp:p,h,t,d,s=0 $ Garde-Corps
5867   44   -2.7       -5867                          imp:n=1 imp:p,h,t,d,s=0 
5868   44   -2.7       -5868                          imp:n=1 imp:p,h,t,d,s=0 
5869   44   -2.7       -5869                          imp:n=1 imp:p,h,t,d,s=0 
5870   44   -2.7       -5870                          imp:n=1 imp:p,h,t,d,s=0 
5871   44   -2.7       -5871                          imp:n=1 imp:p,h,t,d,s=0
5872   44   -2.7       -5872                          imp:n=1 imp:p,h,t,d,s=0
5873   44   -2.7       -5873                          imp:n=1 imp:p,h,t,d,s=0
5874   44   -2.7       -5874                          imp:n=1 imp:p,h,t,d,s=0
5875   44   -2.7       -5875                          imp:n=1 imp:p,h,t,d,s=0
c ----- Escalier plateforme -----
5901   14   -7.8212    -5901 5902 5903                imp:n=1 imp:p,h,t,d,s=0 $ structure
5902   12   -0.0013  -5902:-5903                    imp:n=1 imp:p,h,t,d,s=0 $ air structure
5904   14   -7.8212    -5904 5905 5906 5907 5908      imp:n=1 imp:p,h,t,d,s=0 $ structure +Y
5905   12   -0.0013  -5905:-5906:-5907:-5908        imp:n=1 imp:p,h,t,d,s=0 $ air structure +Y
5909   14   -7.8212    -5909 5910 5911 5912 5913      imp:n=1 imp:p,h,t,d,s=0 $ structure -Y
5910   12   -0.0013  -5910:-5911:-5912:-5913        imp:n=1 imp:p,h,t,d,s=0 $ air structure -Y
5914   14   -7.8212    -5914 5915                     imp:n=1 imp:p,h,t,d,s=0 $ Potaux +X+Y
5915   12   -0.0013  -5915                          imp:n=1 imp:p,h,t,d,s=0 $ Air Potaux +X+Y
5916   14   -7.8212    -5916 5917                     imp:n=1 imp:p,h,t,d,s=0 $ Potaux +X-Y
5917   12   -0.0013  -5917                          imp:n=1 imp:p,h,t,d,s=0 $ Air Potaux +X-Y
5918   14   -7.8212    -5918 5919 5955                imp:n=1 imp:p,h,t,d,s=0 $ Potaux -X+Y
5919   12   -0.0013  -5919      5955                imp:n=1 imp:p,h,t,d,s=0 $ Air Potaux -X+Y
5920   14   -7.8212    -5920 5921 5955                imp:n=1 imp:p,h,t,d,s=0 $ Potaux -X-Y
5921   12   -0.0013  -5921      5955                imp:n=1 imp:p,h,t,d,s=0 $ Air Potaux -X-Y
5922   14   -7.8212    -5922 5923 5918 5946           imp:n=1 imp:p,h,t,d,s=0 $ Barre +Y 
5923   12   -0.0013  -5923      5918 5946           imp:n=1 imp:p,h,t,d,s=0 $ Air Barre +Y
5924   14   -7.8212    -5924 5925 5920 5946           imp:n=1 imp:p,h,t,d,s=0 $ Barre -Y
5925   12   -0.0013  -5925      5920 5946           imp:n=1 imp:p,h,t,d,s=0 $ Air Barre -Y
5926   14   -7.8212    -5926 5927                     imp:n=1 imp:p,h,t,d,s=0 $ Barre +X
5927   12   -0.0013  -5927                          imp:n=1 imp:p,h,t,d,s=0 $ Air Barre +X
5928   39   -0.924     -5928:-5929:-5930              imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis
c ----- Marches -----
5931   14   -7.8212    -5931 5932                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 1 
5932   12   -0.0013  -5932 5933                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 1
5933   39   -0.924     -5933                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 1
5934   14   -7.8212    -5934 5935                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 2
5935   12   -0.0013  -5935 5936                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 2
5936   39   -0.924     -5936                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 2
5937   14   -7.8212    -5937 5938                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 3 
5938   12   -0.0013  -5938 5939                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 3
5939   39   -0.924     -5939                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 3
5940   14   -7.8212    -5940 5941                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 4
5941   12   -0.0013  -5941 5942                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 4
5942   39   -0.924     -5942                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 4
5943   14   -7.8212    -5943 5944                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 5
5944   12   -0.0013  -5944 5945                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 5
5945   39   -0.924     -5945                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 5
5946   14   -7.8212    -5946 5947 5922 5923 5924 5925 imp:n=1 imp:p,h,t,d,s=0 $ Marche 6
5947   12   -0.0013  -5947 5948 5922 5923 5924 5925 imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 6
5948   39   -0.924     -5948                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 6
5949   14   -7.8212    -5949 5950                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 7
5950   12   -0.0013  -5950 5951                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 7
5951   39   -0.924     -5951                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 7
5952   14   -7.8212    -5952 5953                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 8
5953   12   -0.0013  -5953 5954                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 8
5954   39   -0.924     -5954                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 8
5955   14   -7.8212    -5955 5956                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 9
5956   12   -0.0013  -5956 5957 5918 5919 5920 5921 imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 9
5957   39   -0.924     -5957                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 9
5958   14   -7.8212    -5958 5959                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 10
5959   12   -0.0013  -5959 5960                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 10
5960   39   -0.924     -5960                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 10
c ----- Garde-Corps -----
5961   44   -2.7       -5961 5928 5929 5930 5909 5910 imp:n=1 imp:p,h,t,d,s=0 $ Garde-Corps
5962   44   -2.7       -5962                          imp:n=1 imp:p,h,t,d,s=0
5963   29   -7.8       -5963:-5964:-5965:-5966:-5967: &
                       -5968:-5969:-5970:-5971        imp:n=1 imp:p,h,t,d,s=0 $ Garde-Corps Marches -Y
5972   29   -7.8       -5972:-5973:-5974:-5975:-5976: &
                       -5977:-5978:-5979:-5980        imp:n=1 imp:p,h,t,d,s=0 $ Garde-Corps Marches -Y
5981   12   -0.0013  -5981                          &
         5914 5916 5918 5920 5922 5924 5926 5931 5934 &
         5937 5940 5943 5946 5949 5952 5955 5958 5972 &
         5973 5974 5975 5976 5977 5978 5979 5980 5963 &
         5964 5965 5966 5967 5968 5969 5970 5971 5901 &
         5904 5909 5928 5929 5930 5961 5962 6919      imp:n=1 imp:p,h,t,d,s=0 $ Englobant escalier
c ----- Plateforme Canon + 4 plots b�ton + Canon -----
6001   43   -1.4860    -6001 6002                     imp:n=1 imp:p,h,t,d,s=0 $ Cadre         
6002   12   -0.0013  -6002                          imp:n=1 imp:p,h,t,d,s=0 $ Air Cadre     
6003   43   -1.4860    -6003 6004                     imp:n=1 imp:p,h,t,d,s=0 $ Barreaux      
6004   12   -0.0013  -6004                          imp:n=1 imp:p,h,t,d,s=0 $ Air Barreaux  
6005   43   -1.4860    -6005 6003                     imp:n=1 imp:p,h,t,d,s=0 $ Pieds         
6006   43   -1.4860    -6006 6003                  &
       imp:n=1 imp:p,h,t,d,s=0                 
6007   43   -1.4860    -6007 6003                  &
       imp:n=1 imp:p,h,t,d,s=0                 
6008   43   -1.4860    -6008 6003                  &
       imp:n=1 imp:p,h,t,d,s=0                 
6009   14   -7.8212    -6009                          imp:n=1 imp:p,h,t,d,s=0 $ Plateau       
6010   43   -1.4860    -6010                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds         
6011   43   -1.4860    -6011                       &
       imp:n=1 imp:p,h,t,d,s=0                 
6012   43   -1.4860    -6012                       &
       imp:n=1 imp:p,h,t,d,s=0                 
6013   43   -1.4860    -6013                       &
       imp:n=1 imp:p,h,t,d,s=0                 
6014   39   -0.1832    -6014                          imp:n=1 imp:p,h,t,d,s=0 $ Canon 300 kg  
6015   39   -0.1832    -6015                          imp:n=1 imp:p,h,t,d,s=0 $ Canon Tube m�m
6016   11   -2.4       -6016                          imp:n=1 imp:p,h,t,d,s=0 $ Plots b�ton   
6017   11   -2.4       -6017                       &
       imp:n=1 imp:p,h,t,d,s=0                 
6018   11   -2.4       -6018                       &
       imp:n=1 imp:p,h,t,d,s=0                 
6019   11   -2.4       -6019                       &
       imp:n=1 imp:p,h,t,d,s=0                 
6020   43   -1.4860    -6020                          imp:n=1 imp:p,h,t,d,s=0 $ Tube support  
6021   43   -1.4860    -6021 6020                     imp:n=1 imp:p,h,t,d,s=0 $ Barres support
6022   43   -1.4860    -6022 6020                     imp:n=1 imp:p,h,t,d,s=0 $ Barres support
c ----- Structure bleue -----
6031   14   -7.8212    -6031 6032                     imp:n=1 imp:p,h,t,d,s=0 $ Plateau 
6032   12   -0.0013  -6032                          imp:n=1 imp:p,h,t,d,s=0 $ Air 
6033   14   -7.8212    -6033 6034 6035 6036 6037      imp:n=1 imp:p,h,t,d,s=0 $ Rail -Y 
6034   12   -0.0013  -6034                          imp:n=1 imp:p,h,t,d,s=0 $ Air 
6035   12   -0.0013  -6035                          imp:n=1 imp:p,h,t,d,s=0  
6036   12   -0.0013  -6036                          imp:n=1 imp:p,h,t,d,s=0  
6037   12   -0.0013  -6037                          imp:n=1 imp:p,h,t,d,s=0  
6038   14   -7.8212    -6038 6039 6040 6041 6042      imp:n=1 imp:p,h,t,d,s=0 $ Rail -Y 
6039   12   -0.0013  -6039                          imp:n=1 imp:p,h,t,d,s=0 $ Air 
6040   12   -0.0013  -6040                          imp:n=1 imp:p,h,t,d,s=0  
6041   12   -0.0013  -6041                          imp:n=1 imp:p,h,t,d,s=0  
6042   12   -0.0013  -6042                          imp:n=1 imp:p,h,t,d,s=0  
6043   29   -7.8       -6043                          imp:n=1 imp:p,h,t,d,s=0 $ Tiges 
6044   29   -7.8       -6044                          imp:n=1 imp:p,h,t,d,s=0  
6045   29   -7.8       -6045                          imp:n=1 imp:p,h,t,d,s=0  
6046   29   -7.8       -6046                          imp:n=1 imp:p,h,t,d,s=0  
6047   29   -7.8       -6047                          imp:n=1 imp:p,h,t,d,s=0  
6048   29   -7.8       -6048                          imp:n=1 imp:p,h,t,d,s=0  
6049   14   -7.8212    -6049 6050 6051 6052 6053 6054 6055 &
                        6056 6057 6058 6059 6060 6061 imp:n=1 imp:p,h,t,d,s=0 $ Gros rail 
6050   12   -0.0013  -6050 6701 6758                imp:n=1 imp:p,h,t,d,s=0 $ Air sup 
6051   12   -0.0013  -6051 7070 7071 7074           imp:n=1 imp:p,h,t,d,s=0 $ Air -Y 
6052   12   -0.0013  -6052 7070 7071 7074           imp:n=1 imp:p,h,t,d,s=0 $ Air +Y 
6053   12   -0.0013  -6053                          imp:n=1 imp:p,h,t,d,s=0 $ Trous 
6054   12   -0.0013  -6054                          imp:n=1 imp:p,h,t,d,s=0  
6055   12   -0.0013  -6055                          imp:n=1 imp:p,h,t,d,s=0  
6056   12   -0.0013  -6056                          imp:n=1 imp:p,h,t,d,s=0  
6057   12   -0.0013  -6057                          imp:n=1 imp:p,h,t,d,s=0  
6058   12   -0.0013  -6058                          imp:n=1 imp:p,h,t,d,s=0  
6059   12   -0.0013  -6059                          imp:n=1 imp:p,h,t,d,s=0  
6060   12   -0.0013  -6060                          imp:n=1 imp:p,h,t,d,s=0  
6061   12   -0.0013  -6061                          imp:n=1 imp:p,h,t,d,s=0
6062   43   -1.3800    -6062                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds
6063   43   -1.3800    -6063                          imp:n=1 imp:p,h,t,d,s=0 
6064   43   -1.3800    -6064                          imp:n=1 imp:p,h,t,d,s=0 
6065   43   -1.3800    -6065                          imp:n=1 imp:p,h,t,d,s=0 
6066   43   -1.3800    -6066                          imp:n=1 imp:p,h,t,d,s=0 
6067   43   -1.3800    -6067                          imp:n=1 imp:p,h,t,d,s=0 
6068   43   -1.3800    -6068 6063                     imp:n=1 imp:p,h,t,d,s=0 $ Barres horizontales
6069   43   -1.3800    -6069 6063                     imp:n=1 imp:p,h,t,d,s=0 
6070   43   -1.3800    -6070 6066                     imp:n=1 imp:p,h,t,d,s=0 
6071   43   -1.3800    -6071 6066                     imp:n=1 imp:p,h,t,d,s=0 
6072   43   -1.3800    -6072                          imp:n=1 imp:p,h,t,d,s=0 
6073   43   -1.3800    -6073                          imp:n=1 imp:p,h,t,d,s=0 
6074   43   -1.3800    -6074                          imp:n=1 imp:p,h,t,d,s=0 
6075   43   -1.3800    -6075                          imp:n=1 imp:p,h,t,d,s=0 
6076   43   -1.3800    -6076                          imp:n=1 imp:p,h,t,d,s=0 
6077   43   -1.3800    -6077                          imp:n=1 imp:p,h,t,d,s=0 
6078   43   -1.3800    -6078                          imp:n=1 imp:p,h,t,d,s=0 $ Barres diag=verticales
6079   43   -1.3800    -6079                          imp:n=1 imp:p,h,t,d,s=0 
6080   43   -1.3800    -6080                          imp:n=1 imp:p,h,t,d,s=0 
6081   43   -1.3800    -6081                          imp:n=1 imp:p,h,t,d,s=0 
6082   43   -1.3800    -6082                          imp:n=1 imp:p,h,t,d,s=0 
6083   43   -1.3800    -6083                          imp:n=1 imp:p,h,t,d,s=0 $ Barres diag=horizontales
6084   43   -1.3800    -6084                          imp:n=1 imp:p,h,t,d,s=0 
6085   14   -7.8212    -6085 6087                     imp:n=1 imp:p,h,t,d,s=0 $ Poutres en U
6086   14   -7.8212    -6086 6088                     imp:n=1 imp:p,h,t,d,s=0 
6087   12   -0.0013  -6087                          imp:n=1 imp:p,h,t,d,s=0 $ Air
6088   12   -0.0013  -6088                          imp:n=1 imp:p,h,t,d,s=0
c ----- Portiques gris -----
6090   43   -2.1899    -6090                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds -Y
6091   43   -2.1899    -6091                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds +Y
6092   43   -2.1899    -6092                          imp:n=1 imp:p,h,t,d,s=0 $ Barre
6093   29   -7.8       -6093                          imp:n=1 imp:p,h,t,d,s=0 $ Tiges
6094   29   -7.8       -6094                          imp:n=1 imp:p,h,t,d,s=0
6095   29   -7.8       -6095 6093 6094 6096           imp:n=1 imp:p,h,t,d,s=0 $ Barre bleu
6096   12   -0.0013  -6096                          imp:n=1 imp:p,h,t,d,s=0 $ Aire Barre bleu
6097   43   -2.1899    -6097                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds -Y
6098   43   -2.1899    -6098                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds +Y
6099   43   -2.1899    -6099                          imp:n=1 imp:p,h,t,d,s=0 $ Barre
6100   29   -7.8       -6100                          imp:n=1 imp:p,h,t,d,s=0 $ Tiges
6101   29   -7.8       -6101                          imp:n=1 imp:p,h,t,d,s=0
6102   29   -7.8       -6102 6100 6101 6103           imp:n=1 imp:p,h,t,d,s=0 $ Barre bleu
6103   12   -0.0013  -6103                          imp:n=1 imp:p,h,t,d,s=0 $ Aire Barre bleu
6104   43   -2.1899    -6104                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds -Y
6105   43   -2.1899    -6105                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds +Y
6106   43   -2.1899    -6106                          imp:n=1 imp:p,h,t,d,s=0 $ Barre
6107   29   -7.8       -6107                          imp:n=1 imp:p,h,t,d,s=0 $ Tiges
6108   29   -7.8       -6108                          imp:n=1 imp:p,h,t,d,s=0
6109   29   -7.8       -6109 6107 6108 6110           imp:n=1 imp:p,h,t,d,s=0 $ Barre bleu
6110   12   -0.0013  -6110                          imp:n=1 imp:p,h,t,d,s=0 $ Aire Barre bleu
6111   43   -2.1899    -6111                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds -Y
6112   43   -2.1899    -6112                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds +Y
6113   43   -2.1899    -6113                          imp:n=1 imp:p,h,t,d,s=0 $ Barre
6114   29   -7.8       -6114                          imp:n=1 imp:p,h,t,d,s=0 $ Tiges
6115   29   -7.8       -6115                          imp:n=1 imp:p,h,t,d,s=0
6116   29   -7.8       -6116 6114 6115 6117           imp:n=1 imp:p,h,t,d,s=0 $ Barre bleu
6117   12   -0.0013  -6117                          imp:n=1 imp:p,h,t,d,s=0 $ Aire Barre bleu
6118   11   -2.4       -6118                          imp:n=1 imp:p,h,t,d,s=0 $ Blocs B�ton
6119   11   -2.4       -6119                          imp:n=1 imp:p,h,t,d,s=0
6120   11   -2.4       -6120                          imp:n=1 imp:p,h,t,d,s=0
c ----- Support Cam�ra -----
6121   43   -2.445     -6121                          imp:n=1 imp:p,h,t,d,s=0 $ Poteau
6122   29   -7.8       -6122                          imp:n=1 imp:p,h,t,d,s=0 $ Tiges
6123   29   -7.8       -6123                          imp:n=1 imp:p,h,t,d,s=0 
6124   14   -7.8212    -6124 6122                     imp:n=1 imp:p,h,t,d,s=0 $ Rondelles
6125   14   -7.8212    -6125 6123                     imp:n=1 imp:p,h,t,d,s=0 
6126   44   -2.7       -6126 6127 6128 6129 6143      imp:n=1 imp:p,h,t,d,s=0 $ Support cam�ra
6127   12   -0.0013  -6127:-6128:-6129              imp:n=1 imp:p,h,t,d,s=0 $ air support cam�ra
6130   29   -7.8       -6130                          imp:n=1 imp:p,h,t,d,s=0 $ Tiges
6131   29   -7.8       -6131                          imp:n=1 imp:p,h,t,d,s=0 
6132   29   -7.8       -6132                          imp:n=1 imp:p,h,t,d,s=0 
6133   53   -1.38      -6133 6134                     imp:n=1 imp:p,h,t,d,s=0 $ Plaque cam�ra 1
6134   12   -0.0013  -6134                          imp:n=1 imp:p,h,t,d,s=0 $ Air plaque cam�ra 1
6135   44   -2.7       -6135                          imp:n=1 imp:p,h,t,d,s=0 $ Plaque support sup
6136   44   -2.7       -6136                          imp:n=1 imp:p,h,t,d,s=0 
6137   12   -0.0013  -6137                          imp:n=1 imp:p,h,t,d,s=0 $ Air Plaque support sup
6138   53   -1.38      -6138                          imp:n=1 imp:p,h,t,d,s=0 $ Plaque cam�ra 2
6139   29   -7.8       -6139                          imp:n=1 imp:p,h,t,d,s=0 $ Tiges
6140   29   -7.8       -6140                          imp:n=1 imp:p,h,t,d,s=0 
6141   29   -7.8       -6141                          imp:n=1 imp:p,h,t,d,s=0 
6142   53   -1.38      -6142                          imp:n=1 imp:p,h,t,d,s=0 $ Plaque cam�ra 3
6143   53   -1.38      -6143                          imp:n=1 imp:p,h,t,d,s=0 $ Plaque cam�ra 0
C ************************************ C
C ***** PLATEFORME ET LIGNE T400 ***** C
C ************************************ C
c ----- T400 - Structure support -----
6150   43   -1.3800    -6150                          imp:n=1 imp:p,h,t,d,s=0 $ Structure -X haut
6151   43   -1.3800    -6151                          imp:n=1 imp:p,h,t,d,s=0 
6152   43   -1.3800    -6152                          imp:n=1 imp:p,h,t,d,s=0 
6153   43   -1.3800    -6153                          imp:n=1 imp:p,h,t,d,s=0 
6154   43   -1.3800    -6154                          imp:n=1 imp:p,h,t,d,s=0 
6155   43   -1.3800    -6155                          imp:n=1 imp:p,h,t,d,s=0 
6156   43   -1.3800    -6156                          imp:n=1 imp:p,h,t,d,s=0 $ Structure -X bas
6157   43   -1.3800    -6157                          imp:n=1 imp:p,h,t,d,s=0 
6158   43   -1.3800    -6158                          imp:n=1 imp:p,h,t,d,s=0 
6159   43   -1.3800    -6159                          imp:n=1 imp:p,h,t,d,s=0 
6160   43   -1.3800    -6160                          imp:n=1 imp:p,h,t,d,s=0 
6161   43   -1.3800    -6161                          imp:n=1 imp:p,h,t,d,s=0 $ Renforts
6162   43   -1.3800    -6162                          imp:n=1 imp:p,h,t,d,s=0 
6163   43   -1.3800    -6163                          imp:n=1 imp:p,h,t,d,s=0 
6164   43   -1.3800    -6164                          imp:n=1 imp:p,h,t,d,s=0 
6165   43   -1.3800    -6165 6156                     imp:n=1 imp:p,h,t,d,s=0 $ Pieds
6166   43   -1.3800    -6166 6156                     imp:n=1 imp:p,h,t,d,s=0 
6167   43   -1.3800    -6167 6157                     imp:n=1 imp:p,h,t,d,s=0 
6168   43   -1.3800    -6168 6157                     imp:n=1 imp:p,h,t,d,s=0 
6169   43   -1.3800    -6169                          imp:n=1 imp:p,h,t,d,s=0 $ Structure milieu
6170   43   -1.3800    -6170                          imp:n=1 imp:p,h,t,d,s=0 
6171   43   -1.3800    -6171                          imp:n=1 imp:p,h,t,d,s=0 
6172   43   -1.3800    -6172                          imp:n=1 imp:p,h,t,d,s=0 
6173   43   -1.3800    -6173                          imp:n=1 imp:p,h,t,d,s=0 $ Barres
6174   43   -1.3800    -6174                          imp:n=1 imp:p,h,t,d,s=0 
6175   43   -1.3800    -6175                          imp:n=1 imp:p,h,t,d,s=0 
6176   43   -1.3800    -6176                          imp:n=1 imp:p,h,t,d,s=0 
6177   43   -1.3800    -6177 6171                     imp:n=1 imp:p,h,t,d,s=0 $ Pieds
6178   43   -1.3800    -6178 6172                     imp:n=1 imp:p,h,t,d,s=0
6179   43   -1.3800    -6179 6171                     imp:n=1 imp:p,h,t,d,s=0
6180   43   -1.3800    -6180 6172                     imp:n=1 imp:p,h,t,d,s=0
6181   43   -1.3800    -6181                          imp:n=1 imp:p,h,t,d,s=0 $ Structure milieu sup
6182   43   -1.3800    -6182                          imp:n=1 imp:p,h,t,d,s=0 
6183   43   -1.3800    -6183                          imp:n=1 imp:p,h,t,d,s=0
6184   43   -1.3800    -6184                          imp:n=1 imp:p,h,t,d,s=0
6185   43   -1.3800    -6185                          imp:n=1 imp:p,h,t,d,s=0
6186   43   -1.3800    -6186                          imp:n=1 imp:p,h,t,d,s=0
6187   43   -1.3800    -6187                          imp:n=1 imp:p,h,t,d,s=0
6188   43   -1.3800    -6188                          imp:n=1 imp:p,h,t,d,s=0
6189   43   -1.3800    -6189                          imp:n=1 imp:p,h,t,d,s=0 $ Structure +X
6190   43   -1.3800    -6190                          imp:n=1 imp:p,h,t,d,s=0 
6191   43   -1.3800    -6191                          imp:n=1 imp:p,h,t,d,s=0 
6192   43   -1.3800    -6192                          imp:n=1 imp:p,h,t,d,s=0 
6193   43   -1.3800    -6193                          imp:n=1 imp:p,h,t,d,s=0 
6194   43   -1.3800    -6194                          imp:n=1 imp:p,h,t,d,s=0 
6195   43   -1.3800    -6195                          imp:n=1 imp:p,h,t,d,s=0 
6196   43   -1.3800    -6196                          imp:n=1 imp:p,h,t,d,s=0 
6197   43   -1.3800    -6197                          imp:n=1 imp:p,h,t,d,s=0 
6198   43   -1.3800    -6198                          imp:n=1 imp:p,h,t,d,s=0 
6199   43   -1.3800    -6199 6189 6194                imp:n=1 imp:p,h,t,d,s=0 $ Pieds
6200   43   -1.3800    -6200 6189 6194 6205           imp:n=1 imp:p,h,t,d,s=0 
6201   43   -1.3800    -6201 6189 6194                imp:n=1 imp:p,h,t,d,s=0 
6202   43   -1.3800    -6202 6190 6195                imp:n=1 imp:p,h,t,d,s=0 
6203   43   -1.3800    -6203 6190 6195 6206           imp:n=1 imp:p,h,t,d,s=0 
6204   43   -1.3800    -6204 6190 6195                imp:n=1 imp:p,h,t,d,s=0 
6205   43   -1.3800    -6205                          imp:n=1 imp:p,h,t,d,s=0 $ Barre diag
6206   43   -1.3800    -6206                          imp:n=1 imp:p,h,t,d,s=0
6207   29   -7.8       -6207                          imp:n=1 imp:p,h,t,d,s=0 $ Tiges
6208   29   -7.8       -6208                          imp:n=1 imp:p,h,t,d,s=0  
6209   29   -7.8       -6209                          imp:n=1 imp:p,h,t,d,s=0  
6210   29   -7.8       -6210                          imp:n=1 imp:p,h,t,d,s=0  
6211   29   -7.8       -6211                          imp:n=1 imp:p,h,t,d,s=0  
6212   29   -7.8       -6212                          imp:n=1 imp:p,h,t,d,s=0
6213   14   -7.8212    -6213                          imp:n=1 imp:p,h,t,d,s=0 $ Plateau
6214   14   -7.8212    -6214 6216 6217 6218 6219      imp:n=1 imp:p,h,t,d,s=0 $ Poutres U
6215   14   -7.8212    -6215 6220 6221 6222 6223      imp:n=1 imp:p,h,t,d,s=0   
6216   12   -0.0013  -6216                          imp:n=1 imp:p,h,t,d,s=0 $ Air Poutres
6217   12   -0.0013  -6217                          imp:n=1 imp:p,h,t,d,s=0   
6218   12   -0.0013  -6218                          imp:n=1 imp:p,h,t,d,s=0   
6219   12   -0.0013  -6219                          imp:n=1 imp:p,h,t,d,s=0   
6220   12   -0.0013  -6220                          imp:n=1 imp:p,h,t,d,s=0   
6221   12   -0.0013  -6221                          imp:n=1 imp:p,h,t,d,s=0   
6222   12   -0.0013  -6222                          imp:n=1 imp:p,h,t,d,s=0   
6223   12   -0.0013  -6223                          imp:n=1 imp:p,h,t,d,s=0   
6224   23   -7.9       -6224                          imp:n=1 imp:p,h,t,d,s=0 $ Traverses
6225   23   -7.9       -6225                          imp:n=1 imp:p,h,t,d,s=0 
6226   23   -7.9       -6226                          imp:n=1 imp:p,h,t,d,s=0 
6227   23   -7.9       -6227                          imp:n=1 imp:p,h,t,d,s=0 
6228   23   -7.9       -6228                          imp:n=1 imp:p,h,t,d,s=0 
6229   23   -7.9       -6229                          imp:n=1 imp:p,h,t,d,s=0 
6230   23   -7.9       -6230                          imp:n=1 imp:p,h,t,d,s=0 
6231   23   -7.9       -6231                          imp:n=1 imp:p,h,t,d,s=0 
6232   23   -7.9       -6232 6233                     imp:n=1 imp:p,h,t,d,s=0 $ Rails
6233   12   -0.0013  -6233                          imp:n=1 imp:p,h,t,d,s=0   
6234   23   -7.9       -6234 6235                     imp:n=1 imp:p,h,t,d,s=0    
6235   12   -0.0013  -6235                          imp:n=1 imp:p,h,t,d,s=0
6236   23   -7.9       -6236:-6237:-6238:-6239       imp:n=1 imp:p,h,t,d,s=0 $ Rails Guides
6240   20   -0.730     -6240 6241 6169 6170 6171 6172 imp:n=1 imp:p,h,t,d,s=0 $ Caisson en bois
6241   12   -0.0013  -6241 6150 6151 6152 6153 6154 6155 &
                             6156 6157 6158 6159 6160 6161 &
                        6162 6163 6164 6165 6166 6167 6168 &
                        6169 6170 6171 6172       imp:n=1 imp:p,h,t,d,s=0
c ----- Plateforme -----
6242   43   -1.8962    -6242 6243                     imp:n=1 imp:p,h,t,d,s=0 $ Plateforme (idem H Van Gogh)
6243   12   -0.0013  -6243 6245 6246 6247 6249 6250 &
                             6251                     imp:n=1 imp:p,h,t,d,s=0 $ Air Plateforme     
6244   39   -0.924     -6244                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotis
6245   43   -2.1614    -6245                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds 1
6246   43   -2.1614    -6246                          imp:n=1 imp:p,h,t,d,s=0 
6247   43   -2.1614    -6247                          imp:n=1 imp:p,h,t,d,s=0 
6248   43   -2.1614    -6248                          imp:n=1 imp:p,h,t,d,s=0 
6249   43   -2.1614    -6249                          imp:n=1 imp:p,h,t,d,s=0 $ Pieds 2
6250   43   -2.1614    -6250                          imp:n=1 imp:p,h,t,d,s=0 
6251   43   -2.1614    -6251                          imp:n=1 imp:p,h,t,d,s=0 
6252   43   -2.1614    -6252                          imp:n=1 imp:p,h,t,d,s=0
c ----- Marches -----
6253   43   -0.4971    -6253 6254                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 1 
6254   12   -0.0013  -6254 6255                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 1
6255   39   -0.924     -6255                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 1
6256   43   -0.4971    -6256 6257                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 2
6257   12   -0.0013  -6257 6258                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 2
6258   39   -0.924     -6258                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 2
6259   43   -0.4971    -6259 6260                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 3 
6260   12   -0.0013  -6260 6261                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 3
6261   39   -0.924     -6261                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 3
6262   43   -0.4971    -6262 6263                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 4
6263   12   -0.0013  -6263 6264                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 4
6264   39   -0.924     -6264                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 4
6265   43   -0.4971    -6265 6266                     imp:n=1 imp:p,h,t,d,s=0 $ Marche 5
6266   12   -0.0013  -6266 6267                     imp:n=1 imp:p,h,t,d,s=0 $ Air Marche 5
6267   39   -0.924     -6267                          imp:n=1 imp:p,h,t,d,s=0 $ Caillebotie Marche 5
6268   44   -2.7       -6268                          imp:n=1 imp:p,h,t,d,s=0 $ Garde-Corps
6269   44   -2.7       -6269                          imp:n=1 imp:p,h,t,d,s=0
c ----- Ligne T400 -----
6301   58   -2.69      (-6301 6302):(-6307 6306): &                                 
                       (-6303 6304):(-6308 6306)      imp:n=1 imp:p,h,t,d,s=0 $ Aluminium porte-cible
6302   59   -1.300E-06 (-6302:-6304) 6417             imp:n=1 imp:p,h,t,d,s=0 $ Vide dans le porte-cible
6305   60   -8.96      -6305                          imp:n=1 imp:p,h,t,d,s=0 $ Backing en Cuivre
6306   61   -1.00      -6306 6305 6303                imp:n=1 imp:p,h,t,d,s=0 $ Eau de refroidissement
6309   59   -1.300E-06 -6309                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Int Cone
6310   58   -2.69      -6310 6309                     imp:n=1 imp:p,h,t,d,s=0 $ Aluminium Ext Cone
6311   58   -2.69      -6311 6312                     imp:n=1 imp:p,h,t,d,s=0 $ Aluminium Bride
6312   59   -1.300E-06 -6312                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Bride
6313   59   -1.300E-06 -6313                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Vanne VAT
6314   58   -2.69      (-6314:-6315:-6316) 6313       imp:n=1 imp:p,h,t,d,s=0 $ Corps Vanne VAT
6317   53   -1.38      -6317                          imp:n=1 imp:p,h,t,d,s=0 $ Manche Vanne VAT
6318   58   -2.69      -6318 6310                     imp:n=1 imp:p,h,t,d,s=0 $ "Cible" photo IMG_0219.jpg
6319   58   -2.69      -6319 6318                     imp:n=1 imp:p,h,t,d,s=0 $ �quip. Inf                
6320   58   -2.69      -6320 6318                     imp:n=1 imp:p,h,t,d,s=0 $ �quip. Sup                
6321   58   -2.69      -6321                          imp:n=1 imp:p,h,t,d,s=0
6322   53   -1.38      -6322                          imp:n=1 imp:p,h,t,d,s=0
6323   58   -2.69      -6323 6324                     imp:n=1 imp:p,h,t,d,s=0 $ Aluminium Bride
6324   59   -1.300E-06 -6324                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Bride     
6325   58   -2.69      -6325 6326                     imp:n=1 imp:p,h,t,d,s=0 $ Goulot Module Diag    
6326   59   -1.300E-06 -6326                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Goulot Module Diag
6327   58   -2.69      -6327 6328 6326 6329 6349 6369 &
                                                 6382 imp:n=1 imp:p,h,t,d,s=0 $ Module Diag     
6328   59   -1.300E-06 -6328                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Module Diag
c
6329   59   -1.300E-06  -6329 6336 -6335              imp:n=1 imp:p,h,t,d,s=0 $ Passage diode C
6330   58   -2.69       -6330 6331  6338  -6336       imp:n=1 imp:p,h,t,d,s=0 $ Tube Diode C 
6331   59   -1.300E-06  -6331 6338 -6336              imp:n=1 imp:p,h,t,d,s=0 $ Vide Tube Diode C
6332   36   -8.386      -6332 6333  6339  -6338       imp:n=1 imp:p,h,t,d,s=0 $ Diode C     
6333   59   -1.300E-06  -6333 6339 -6338              imp:n=1 imp:p,h,t,d,s=0 $ Vide Diode C
6334   58   -2.69       -6334 6332  6339  -6338       imp:n=1 imp:p,h,t,d,s=0 $ Fixation Diode C
c
6349   59   -1.300E-06  -6349 6336 -6335              imp:n=1 imp:p,h,t,d,s=0 $ Passage diode A
6350   58   -2.69       -6350 6351  6358  -6336       imp:n=1 imp:p,h,t,d,s=0 $ Tube Diode A     
6351   59   -1.300E-06  -6351 6358 -6336              imp:n=1 imp:p,h,t,d,s=0 $ Vide Tube Diode A
6352   36   -8.386      -6352 6353  6359  -6358       imp:n=1 imp:p,h,t,d,s=0 $ Diode A          
6353   59   -1.300E-06  -6353 6359 -6358              imp:n=1 imp:p,h,t,d,s=0 $ Vide Diode A     
6354   58   -2.69       -6354 6352  6359  -6358       imp:n=1 imp:p,h,t,d,s=0 $ Fixation Diode A
c
6369   59   -1.300E-06  -6369 6336 -6335              imp:n=1 imp:p,h,t,d,s=0 $ Passage diode B
6370   58   -2.69       -6370 6371  6378  -6336       imp:n=1 imp:p,h,t,d,s=0 $ Tube Diode B     
6371   59   -1.300E-06  -6371 6378 -6336              imp:n=1 imp:p,h,t,d,s=0 $ Vide Tube Diode B
6372   36   -8.386      -6372 6373  6379  -6378       imp:n=1 imp:p,h,t,d,s=0 $ Diode B          
6373   59   -1.300E-06  -6373 6379 -6378              imp:n=1 imp:p,h,t,d,s=0 $ Vide Diode B     
6374   58   -2.69       -6374 6372  6379  -6378       imp:n=1 imp:p,h,t,d,s=0 $ Fixation Diode B 
c
6381   58   -2.69      -6381 6382                     imp:n=1 imp:p,h,t,d,s=0 $ Sortie Arr. Diag      
6382   59   -1.300E-06 -6382                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Sortie Arr. Diag 
6383   58   -2.69      -6383 6382                     imp:n=1 imp:p,h,t,d,s=0 $ Bride
6384   58   -2.69      -6384 6388                     imp:n=1 imp:p,h,t,d,s=0 $ Piege � �lectron (6) Bride av
6385   58   -2.69      -6385 6387 6388                imp:n=1 imp:p,h,t,d,s=0 $ Piege � �lectron (6) Tube    
6386   58   -2.69      -6386 6387                     imp:n=1 imp:p,h,t,d,s=0 $ Piege � �lectron (6) Bride ar
6387   59   -1.300E-06 -6387:-6388                    imp:n=1 imp:p,h,t,d,s=0 $ Vide Piege � �lectron (6)
6389   58   -2.69      (-6389:-6390:-6391) 6392       imp:n=1 imp:p,h,t,d,s=0 $ Diaphragme (5) Brides et tube
6392   59   -1.300E-06 -6392                          imp:n=1 imp:p,h,t,d,s=0 $ Diaphragme (5) Vide
6393   58   -2.69      -6393 6394                     imp:n=1 imp:p,h,t,d,s=0 $ Interface vide / cible (4)
6394   59   -1.300E-06 -6394                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Interface            
6395   58   -2.69      -6395 6396                     imp:n=1 imp:p,h,t,d,s=0 $ Tube (3) / (4)            
6396   59   -1.300E-06 -6396                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Tube (3) / (4)       
6397   58   -2.69      -6397 6399                     imp:n=1 imp:p,h,t,d,s=0 $ Vanne manuelle (3)        
6398   58   -2.69      -6398 6399                     imp:n=1 imp:p,h,t,d,s=0 $                           
6399   59   -1.300E-06 -6399                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Vanne manuelle (3)
6400   14   -7.8212    -6400 6401 6403 6399           imp:n=1 imp:p,h,t,d,s=0 $ Pi�ce fonderie (2)     
6401   59   -1.300E-06 -6401                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Pi�ce fonderie (2)
6402   14   -7.8212    -6402 6403 6400                imp:n=1 imp:p,h,t,d,s=0 $ Liaison Pompe / (2)    
6403   59   -1.300E-06 -6403 6401                     imp:n=1 imp:p,h,t,d,s=0 $ Vide Liaison Pompe / (2)
6404   23   -7.9       (-6404:-6405:-6406:-6407) 6408 &
                        6409 6410                     imp:n=1 imp:p,h,t,d,s=0 $ Pompe � vide (13) corps
6408   59   -1.300E-06 -6408:-6409:-6410              imp:n=1 imp:p,h,t,d,s=0 $ Vide Pompe � vide (13)
6411   23   -7.9       -6411                          imp:n=1 imp:p,h,t,d,s=0 $ Plaque canon T400    
6412   39   -0.1832    -6412                          imp:n=1 imp:p,h,t,d,s=0 $ Support canon T400
6413   39   -0.1832    -6413                          imp:n=1 imp:p,h,t,d,s=0 $ Casson canon T400 
6414   39   -0.1832    -6414 6415                     imp:n=1 imp:p,h,t,d,s=0 $ Canon T400
6415   14   -7.8212    -6415 6416                     imp:n=1 imp:p,h,t,d,s=0 $ Tube Canon T400     
6416   59   -1.300E-06 -6416                          imp:n=1 imp:p,h,t,d,s=0 $ Vide Tube Canon T400
c ----- Cible TiD -----                               
6417   40   -4.84      -6417                          imp:n=1 imp:p,h,t,d,s=0 $ Cible TiD
c ----- support module diag, cablages -----           
6418   38   -1.2        6418 -6419 -6420              imp:n=1 imp:p,h,t,d,s=0 $ Cablage
6421   14   -7.8212    -6421                          imp:n=1 imp:p,h,t,d,s=0 $ Plaque support Module diodes
6422   14   -7.8212    -6422 6423 6327                imp:n=1 imp:p,h,t,d,s=0 $ Support Module diodes       
6423   12   -0.0013  -6423 6327                     imp:n=1 imp:p,h,t,d,s=0 $ air Support Module diodes
C ************************** C
C ***** BLOG - RETRAIT ***** C
C ************************** C
6450  19 -0.93     -6450 6451 6486 6487 imp:n=1 imp:p,h,t,d,s=0 $ PEHD
6451  18 -1.693    -6451 6487 imp:n=1 imp:p,h,t,d,s=0 $ Graphite
6452  14 -7.8212   -6452 6454 6455 imp:n=1 imp:p,h,t,d,s=0 $ Chassis
6453  14 -7.8212   -6453 6456 6457 imp:n=1 imp:p,h,t,d,s=0
6454  12 -0.0013     -6454 imp:n=1 imp:p,h,t,d,s=0
6455  12 -0.0013     -6455 imp:n=1 imp:p,h,t,d,s=0
6456  12 -0.0013     -6456 imp:n=1 imp:p,h,t,d,s=0
6457  12 -0.0013     -6457 imp:n=1 imp:p,h,t,d,s=0
6458  14 -7.8212   -6458 6459 6452 6454 6455 6453 6456 6457 &
      imp:n=1 imp:p,h,t,d,s=0 $ UPE 220
6459  12 -0.0013  -6459 #6462 6452 6454 6455 6453 &
    6456 6457 imp:n=1 imp:p,h,t,d,s=0
6460  14 -7.8212   -6460 6461 6452 6454 6455 6453 6456 &
    6457 imp:n=1 imp:p,h,t,d,s=0
6461  12 -0.0013  -6461 #6462 6452 6454 6455 6453 &
    6456 6457 imp:n=1 imp:p,h,t,d,s=0
6462  14 -7.8212   -6462 6463 #6458 #6460 imp:n=1 imp:p,h,t,d,s=0
6463  12 -0.0013     -6463 6458 6459 6460 6461 imp:n=1 imp:p,h,t,d,s=0
6464  14 -7.8212   -6464:-6465:-6466 imp:n=1 imp:p,h,t,d,s=0 $ Patins
6467  14 -7.8212   -6467:-6468:-6469 imp:n=1 imp:p,h,t,d,s=0
6470  14 -7.8212   -6470:-6471:-6472 imp:n=1 imp:p,h,t,d,s=0
6473  14 -7.8212   -6473:-6474:-6475 imp:n=1 imp:p,h,t,d,s=0
6476  14 -7.8212   -6476:-6477:-6478 imp:n=1 imp:p,h,t,d,s=0
6479  14 -7.8212   -6479:-6480:-6481 imp:n=1 imp:p,h,t,d,s=0
6482  23 -7.9      -6482:-6483:-6484:-6485 imp:n=1 imp:p,h,t,d,s=0 $ Roues :-)
6486  12 -0.0013     -6486:-6487 imp:n=1 imp:p,h,t,d,s=0 $ Trou face arri�re Blog
c ----- Englobants BLOG RETRAIT -----                                     
6488  12 -0.0013     -6488 6458 6460 6462 imp:n=1 imp:p,h,t,d,s=0 $ Englobant sous BLOG RETRAIT
6489  12 -0.0013  -6489 6458 6460 6452 6464 6465 &
    6466 6467 6468 6469 6470 6471 6472 6482 6483 imp:n=1 &
    imp:p,h,t,d,s=0 $ Englobant rail -Y BLOG RETRAIT
6490  12 -0.0013  -6490 6458 6460 6453 6473 6474 &
    6475 6476 6477 6478 6479 6480 6481 6484 6485 imp:n=1 &
    imp:p,h,t,d,s=0 $ Englobant rail -Y BLOG RETRAIT
C *********************** C
C ***** CANEL - SUD ***** C
C *********************** C
c ----- Support Canel -----
6500  43 -1.7645   -6500 6501 imp:n=1 imp:p,h,t,d,s=0 $ Cadre vertical -Y
6501  12 -0.0013     -6501 6508 6510 6511 imp:n=1 imp:p,h,t,d,s=0
6502  43 -1.7645   -6502 6503 imp:n=1 imp:p,h,t,d,s=0 $ Cadre vertical +Y
6503  12 -0.0013     -6503 6509 6512 6513 imp:n=1 imp:p,h,t,d,s=0
6504  43 -1.7645   -6504 6505 6500 6502 imp:n=1 imp:p,h,t,d,s=0 $ Gd cadre
6505  12 -0.0013     -6505 imp:n=1 imp:p,h,t,d,s=0
6506  43 -1.7645   -6506 6507 6500 6502 imp:n=1 imp:p,h,t,d,s=0
6507  12 -0.0013     -6507 imp:n=1 imp:p,h,t,d,s=0
6508  43 -1.7645   -6508 imp:n=1 imp:p,h,t,d,s=0
6509  43 -1.7645   -6509 imp:n=1 imp:p,h,t,d,s=0
6510  43 -1.7645   -6510 imp:n=1 imp:p,h,t,d,s=0
6511  43 -1.7645   -6511 imp:n=1 imp:p,h,t,d,s=0
6512  43 -1.7645   -6512 imp:n=1 imp:p,h,t,d,s=0
6513  43 -1.7645   -6513 imp:n=1 imp:p,h,t,d,s=0
6514  43 -1.7645   -6514 6515 imp:n=1 imp:p,h,t,d,s=0 $ Petit cadre
6515  12 -0.0013     -6515 imp:n=1 imp:p,h,t,d,s=0
6516  43 -1.7645   -6516 6517 imp:n=1 imp:p,h,t,d,s=0
6517  12 -0.0013     -6517 imp:n=1 imp:p,h,t,d,s=0
6518  43 -1.7645   -6518 imp:n=1 imp:p,h,t,d,s=0
6519  43 -1.7645   -6519 imp:n=1 imp:p,h,t,d,s=0
6520  43 -1.7645   -6520 6521 imp:n=1 imp:p,h,t,d,s=0 $ Plateau inf
6521  12 -0.0013     -6521 imp:n=1 imp:p,h,t,d,s=0
6522  43 -1.7645   -6522 imp:n=1 imp:p,h,t,d,s=0 $ Plateau sup
6523  23 -7.9      -6523:-6524:-6525:-6526 imp:n=1 imp:p,h,t,d,s=0 $ Roues
c ----- Canel -----                                             
6531  27 -0.96     6531 6532 -6533 -6534 6535 -6536 &
    6537 -6538 6539 -6540 6557 6575 imp:n=1 imp:p,h,t,d,s=0 $ 5 cm polyethylene
6541  27 -0.96     6531 6532 -6533 -6534 6536 -6541 &
    6537 -6538 6539 -6540 6544 imp:n=1 imp:p,h,t,d,s=0 $ 10 cm polyethylene
6542  56 -7.87     6531 6532 -6533 -6534 6541 -6542 &
    6537 -6538 6539 -6540 6553 imp:n=1 imp:p,h,t,d,s=0 $ 2 cm acier
6543  27 -0.96     6531 6532 -6533 -6534 6542 -6543 &
    6537 -6538 6539 -6540 6545 6546 imp:n=1 imp:p,h,t,d,s=0 $ 93.5 cm polyethylene
6544  12 -0.0013     -6544 (-6568:6569:-6570:6571:-6572:6573) &
      imp:n=1 imp:p,h,t,d,s=0 $ Air 10 cm polyethylene
6545  12 -0.0013     -6545 6546 6547 imp:n=1 imp:p,h,t,d,s=0 $ Air 93.5 cm polyethylene
6546  27 -0.96     -6546 imp:n=1 imp:p,h,t,d,s=0 $ Poly layer (e=3.5 cm)
6547  56 -7.87     -6547 6542 6548 imp:n=1 imp:p,h,t,d,s=0 $ Grande coquille Fer
6548  56 -7.87     -6548 6542 6549 imp:n=1 imp:p,h,t,d,s=0 $ Petite coquille Fer
6549  57 -19.06    -6549 6542 6550 imp:n=1 imp:p,h,t,d,s=0 $ Grande coquille Uranium
6550  56 -7.87    (-6550 6552 6551):(-6550 6542 -6552) imp:n=1 imp:p,h,t,d,s=0 $ Paroi acier coquille Uranium
6551  57 -19.06    -6551 6552 imp:n=1 imp:p,h,t,d,s=0 $ Petite coquille Uranium
6553  56 -7.87     -6553 6554 imp:n=1 imp:p,h,t,d,s=0 $ Manchon d'acier
6554  57 -19.06    -6554 6555 imp:n=1 imp:p,h,t,d,s=0 $ Manchon Uranium
6555  56 -7.87     -6555 6556 imp:n=1 imp:p,h,t,d,s=0 $ Manchon d'acier
6556  12 -0.0013     -6556 imp:n=1 imp:p,h,t,d,s=0 $ Air autour porte-cible
6557  12 -0.0013     -6557 imp:n=1 imp:p,h,t,d,s=0 $ Cyl. Air dans polyethylene e=5 cm
6568  56 -7.87     (6536 -6541 6568 -6569 6570 -6571 &
    6572 -6573) 6553 imp:n=1 imp:p,h,t,d,s=0 $ Hexagone acier
6574  62 -2.00     -6574 imp:n=1 imp:p,h,t,d,s=0 $ Inside fission chamber
6575  58 -2.69     -6575 6574 imp:n=1 imp:p,h,t,d,s=0 $ Cyl. fission chamber
c ----- Englobant CANEL -----                                         
6578   12   -0.0013  -6578 (-6531:-6532:6533:6534:-6535       &
                              :6543:-6537:6538:-6539:6540)      &
                        (6500 6502 6504 6506 6514 6516 6518     &
                         6519 6520 6522 6523 6524 6525 6526)    &
                         imp:n=1 imp:p,h,t,d,s=0 $ Englobant CANEL
C
C ************************ C
C ***** CHARIOT T400 ***** C
C ************************ C
6601   29   -7.8       -6601                         imp:n=1 imp:p,h,t,d,s=0 $ Suppor Moteur fixe
6602   29   -7.8       -6602                         imp:n=1 imp:p,h,t,d,s=0
6603   29   -7.8       -6603                         imp:n=1 imp:p,h,t,d,s=0
6604   29   -11.7      -6605:-6606                   imp:n=1 imp:p,h,t,d,s=0 $ Rails chariot - suite � un conflit avec le support C�ne la vis est supprim�e, la densit� dispath�e sur les guides
6607   53   -1.38      -6607                         imp:n=1 imp:p,h,t,d,s=0 $ Capot Moteur fixe
6608   42   -2.0       -6608:-6609:-6610:-6611       imp:n=1 imp:p,h,t,d,s=0 $ Moteur fixe
6612   29   -7.8       -6612:-6613                   imp:n=1 imp:p,h,t,d,s=0 $ Plateau support moteur inf
6614   42   -2.0       -6614                         imp:n=1 imp:p,h,t,d,s=0 $ Moteur inf
6615   29   -7.8       -6615                         imp:n=1 imp:p,h,t,d,s=0 $ Base inf carr�e
6616   29   -7.8       -6616                         imp:n=1 imp:p,h,t,d,s=0 $ Plaque support moteur inf+
6617   42   -2.0       -6617                         imp:n=1 imp:p,h,t,d,s=0 $ Moteur inf+
6618   29   -7.8       -6618                         imp:n=1 imp:p,h,t,d,s=0 $ Plateau tournant
6619   29   -7.8       -6619                         imp:n=1 imp:p,h,t,d,s=0
6620   29   -7.8       -6620:(-6626 -6628)           imp:n=1 imp:p,h,t,d,s=0 $ Plaque support moteur sup
6621   29   -7.8       -6621 -6627                   imp:n=1 imp:p,h,t,d,s=0 $ Plaque support detecteur inf
6622   29   -7.8       -6622:-6623:-6624             imp:n=1 imp:p,h,t,d,s=0 $ Plateau Moteur sup
6625   42   -2.0       -6625                         imp:n=1 imp:p,h,t,d,s=0 $ Moteur sup
6629   29   -7.8       -6629 -6639                   imp:n=1 imp:p,h,t,d,s=0 $ Porte-d�tecteur position basse
6630   29   -7.8       -6630:-6631:-6632:-6633       imp:n=1 imp:p,h,t,d,s=0 $ Pieds
6634   29   -7.8       -6634 -6640                   imp:n=1 imp:p,h,t,d,s=0 $ Porte-d�tecteur en position sur�lev�e
6635   29   -7.8       -6635:-6636:-6637:-6638       imp:n=1 imp:p,h,t,d,s=0 $ Pieds
c ----- Pupitre (AMANDE) -----
6641   29   -7.8       -6641 6642                    imp:n=1 imp:p,h,t,d,s=0 $ pied pupitre
6642   12   -0.0013  -6642                           imp:n=1 imp:p,h,t,d,s=0 $ air dans pied pupitre
6643   29   -7.8       -6643 6644                    imp:n=1 imp:p,h,t,d,s=0 $ plateau pupitre
6644   42   -2.0       -6644                         imp:n=1 imp:p,h,t,d,s=0 $ �quipement pupitre
6645   12   -0.0013  -6645 6641 6643 6644            imp:n=1 imp:p,h,t,d,s=0 $ Englobant Pupitre
c
C **************************** C
C ***** CHARIOT VAN GOGH ***** C
C **************************** C
6701   45   -2.79      -6701 6702 6703               imp:n=1 imp:p,h,t,d,s=0 $ Module d'entrainement
6702   12   -0.0013  -6702 6704                      imp:n=1 imp:p,h,t,d,s=0 $ Logements vis sans fin
6703   12   -0.0013  -6703 6705                      imp:n=1 imp:p,h,t,d,s=0 
6704   29   -7.8       -6704                         imp:n=1 imp:p,h,t,d,s=0 $ Vis sans fin
6705   29   -7.8       -6705                         imp:n=1 imp:p,h,t,d,s=0
6706   29   -7.8       -6706                         imp:n=1 imp:p,h,t,d,s=0 $ But� face avt
6707   23   -7.9       -6707 6708                    imp:n=1 imp:p,h,t,d,s=0 $ Cache avt
6708  12 -0.0013     -6708 7064 imp:n=1 imp:p,h,t,d,s=0
6709  45 -2.79     -6709 6714 imp:n=1 imp:p,h,t,d,s=0 $ Plaque basse
6710   45   -2.79      -6710:-6711:-6712:-6713       imp:n=1 imp:p,h,t,d,s=0 $ Tiges
6714   46   -8.00      -6714                         imp:n=1 imp:p,h,t,d,s=0 $ Tige guidage
6715   45   -2.79      -6715 6714 6716 6719          imp:n=1 imp:p,h,t,d,s=0 $ Plaque haute
6716   12   -0.0013  -6716                           imp:n=1 imp:p,h,t,d,s=0 $ Air Plaque haute
6717   45   -2.79      -6717 6718                      imp:n=1 imp:p,h,t,d,s=0 $ Guidage chariot
6718   12   -0.0013  -6718 6714                      imp:n=1 imp:p,h,t,d,s=0 $ Air Guidage chariot
6719   29   -7.8       -6719 6720                      imp:n=1 imp:p,h,t,d,s=0 $ Carter verin
6720   12   -0.0013  -6720 6728                      imp:n=1 imp:p,h,t,d,s=0 $ Air Carter verin
6721   45   -2.79      -6721                           imp:n=1 imp:p,h,t,d,s=0 $ Plaque +Y
6722   45   -2.79      -6722                           imp:n=1 imp:p,h,t,d,s=0 $ Plaque -Y
6723   45   -2.79      -6723                           imp:n=1 imp:p,h,t,d,s=0 $ Plateau verin
6724   45   -2.79      -6724:-6725                     imp:n=1 imp:p,h,t,d,s=0 $ Support plateau verin
6726   14   -7.8212    -6726 6728                      imp:n=1 imp:p,h,t,d,s=0 $ Support moteur
6727   14   -7.8212    -6727 6728 6730                 imp:n=1 imp:p,h,t,d,s=0 $ Gros Cyl
6728   46   -8.00      -6728                           imp:n=1 imp:p,h,t,d,s=0 $ Vis verin
6729   29   -7.8       -6729 6724 6725                 imp:n=1 imp:p,h,t,d,s=0 $ Chape tige verin
6730   14   -7.8212    -6730 6726 6728                 imp:n=1 imp:p,h,t,d,s=0 $ Verin moteur
6731   14   -7.8212    -6731                           imp:n=1 imp:p,h,t,d,s=0 
6732   14   -7.8212    -6732                           imp:n=1 imp:p,h,t,d,s=0 $ Bride
6733   42   -2.0       -6733                           imp:n=1 imp:p,h,t,d,s=0 $ Moteur
6734   45   -2.79      -6734 -6735 6737                imp:n=1 imp:p,h,t,d,s=0 $ Plateau table tournante
6736   45   -2.79      -6736 6737                      imp:n=1 imp:p,h,t,d,s=0
6737   12   -0.0013  -6737                             imp:n=1 imp:p,h,t,d,s=0 $ Air Plateau table tournante
6738   45   -2.79      -6738 -6739                     imp:n=1 imp:p,h,t,d,s=0 $ Rehausse basse
6740   45   -2.79      (-6740:-6741:-6742:-6743) -6739 imp:n=1 imp:p,h,t,d,s=0
6744   45   -2.79      -6744:-6745:-6746               imp:n=1 imp:p,h,t,d,s=0
6747   45   -2.79      -6747 -6748                     imp:n=1 imp:p,h,t,d,s=0
6749   53   -1.38      -6749:-6750:-6751:-6752:-6753:-6754 &
      imp:n=1 imp:p,h,t,d,s=0 $ Bouchons
6755   42   -2.0       -6755                           imp:n=1 imp:p,h,t,d,s=0 $ Aerotech
6756   42   -2.0       -6756                           imp:n=1 imp:p,h,t,d,s=0 $ Moteur
6757   29   -7.8       -6757                           imp:n=1 imp:p,h,t,d,s=0 $ Moteur fixe - tige
6758   45   -2.79      -6758                           imp:n=1 imp:p,h,t,d,s=0 $ Moteur fixe - support
6759   42   -2.0       -6759                           imp:n=1 imp:p,h,t,d,s=0 $ Moteur fixe
6760   42   -2.0      (-6760:-6761):(6762 -6763 -6764) imp:n=1 imp:p,h,t,d,s=0 $ Chaine + Cablage
C *************************************
C ***** BLOC SOURCE VAN GOGH - Cf *****
C *************************************
c Sources Container - Polyethilen and Polyurethan Box
7001  28 -0.96     -7001 7002 7003 7004 imp:n=1 imp:p,h,t,d,s=0 $ Polyurethan ext
7002  27 -0.96     -7002 7003 7004 imp:n=1 imp:p,h,t,d,s=0 $ Polyethilen int
7003  12 -0.0013     -7003 7007 imp:n=1 imp:p,h,t,d,s=0 $ cavit� Cf
7004  12 -0.0013     -7004 7008 imp:n=1 imp:p,h,t,d,s=0 $ cavit� Am-Be
7005  27 -0.96     -7005 imp:n=1 imp:p,h,t,d,s=0 $ Polyethilen bottom block
c Tubes support
7006  23 -7.9      -7006 7007 7008 7011 7012 imp:n=1 imp:p,h,t,d,s=0 $ top plaque
7007  23 -7.9      -7007 7009 7013 imp:n=1 imp:p,h,t,d,s=0 $ tube Cf
7008  23 -7.9      -7008 7010 7017 imp:n=1 imp:p,h,t,d,s=0 $ tube Am-Be
7009  12 -0.0013     -7009 7013 7014 7015 7021 imp:n=1 imp:p,h,t,d,s=0 $ air tube Cf
7010  12 -0.0013  -7010 7017 7018 7019 7026 7115 &
    7101 7103 7104 imp:n=1 imp:p,h,t,d,s=0 $ air tube Am-Be
7011  12 -0.0013     -7011 7021 imp:n=1 imp:p,h,t,d,s=0 $ air top tube Cf
7012  12 -0.0013     -7012 7026 imp:n=1 imp:p,h,t,d,s=0 $ air top tube Am-Be
c Fixed Source Supports
7013  27 -0.96     -7013 7016 imp:n=1 imp:p,h,t,d,s=0 $ bottom part Cf
7014  27 -0.96     -7014 7016 imp:n=1 imp:p,h,t,d,s=0 $ intermediate part Cf
7015  27 -0.96     -7015 7016 imp:n=1 imp:p,h,t,d,s=0 $ upper part Cf
7016  12 -0.0013     -7016 imp:n=1 imp:p,h,t,d,s=0 $ air source Supports Cf
7017  27 -0.96     -7017 7020 imp:n=1 imp:p,h,t,d,s=0 $ bottom part Am-Be
7018  27 -0.96     -7018 7020 imp:n=1 imp:p,h,t,d,s=0 $ intermediate part Am-Be
7019  27 -0.96     -7019 7020 imp:n=1 imp:p,h,t,d,s=0 $ upper part Am-Be
7020  12 -0.0013     -7020 imp:n=1 imp:p,h,t,d,s=0 $ air source Supports Am-Be
c Ejection tube and air volume Cf
7021  31 -2.66     -7021 7022 imp:n=1 imp:p,h,t,d,s=0 $ ejection tube Cf
7022  12 -0.0013     -7022 7014 7015 7027 imp:n=1 imp:p,h,t,d,s=0 $ air Ejection tube Cf
7023  31 -2.66     -7023 7021 imp:n=1 imp:p,h,t,d,s=0 $ inf upper support
7024  31 -2.66     -7024 7021 imp:n=1 imp:p,h,t,d,s=0 $ sup upper support
c Stopper tube Am-Be
7025  27 -0.96     -7025 imp:n=1 imp:p,h,t,d,s=0 $ top part
7026  27 -0.96     -7026 imp:n=1 imp:p,h,t,d,s=0 $ inside part
c Cf Porte-source
7027  24 -2.685    -7027 7028 7099 imp:n=1 imp:p,h,t,d,s=0 $ piston Cf
7099  12 -0.0013     -7099 imp:n=1 imp:p,h,t,d,s=0 $ Air piston Cf
7028  34 -2.710    -7028 imp:n=1 imp:p,h,t,d,s=0 $ Base porte source inf
7029  34 -2.710    -7029 imp:n=1 imp:p,h,t,d,s=0 $ Base porte source sup
7030  34 -2.710    -7030 7031 -7032 imp:n=1 imp:p,h,t,d,s=0 $ Meplat serrage
7033  34 -2.710    -7033 7034 imp:n=1 imp:p,h,t,d,s=0 $ Base porte source sup
7034  34 -2.710    -7034 imp:n=1 imp:p,h,t,d,s=0 $ Reglages inf
7035  34 -2.710    -7035 7031 -7032 imp:n=1 imp:p,h,t,d,s=0 $ Reglages milieu
7036  34 -2.710    -7036 imp:n=1 imp:p,h,t,d,s=0 $ Reglages sup
7037  34 -2.710    -7037 7036 7038 imp:n=1 imp:p,h,t,d,s=0 $ Coiffe
7038  12 -0.0013     -7038 7049 imp:n=1 imp:p,h,t,d,s=0 $ Air Coiffe
7039  34 -2.710    -7039 7031 -7032 imp:n=1 imp:p,h,t,d,s=0 $ Top Coiffe
c Cf source
7040  22 -0.074    -7040 imp:n=1 imp:p,h,t,d,s=0 $ active volume
7041  26 -7.700    -7041 7040 imp:n=1 imp:p,h,t,d,s=0 $ 6A Spacer
7042  26 -7.700    -7042 7043 imp:n=1 imp:p,h,t,d,s=0 $ Cell body
7043  12 -0.0013     -7043 7041 7044 imp:n=1 imp:p,h,t,d,s=0 $ air Cell body
7044  26 -7.700    -7044 7045 imp:n=1 imp:p,h,t,d,s=0 $ Cell lid
7045  12 -0.0013     -7045 imp:n=1 imp:p,h,t,d,s=0 $ air Cell lid
7046  26 -7.700    -7046 imp:n=1 imp:p,h,t,d,s=0 $ 07 Spacer
7047  26 -7.700    -7047 7048 imp:n=1 imp:p,h,t,d,s=0 $ Sheath lid
7048  12 -0.0013     -7048 imp:n=1 imp:p,h,t,d,s=0 $ air Sheath lid
7049  26 -7.700    -7049 7050 imp:n=1 imp:p,h,t,d,s=0 $ Sheath body
7050  12 -0.0013     -7050 7047 7046 7042 imp:n=1 imp:p,h,t,d,s=0 $ air Sheath body
c Cf sphere
7051  12 -0.0013   -7051 7052 7053 imp:n=1 imp:p,h,t,d,s=0 $ sphere
7052  12 -0.0013   -7052 7053 7054 imp:n=1 imp:p,h,t,d,s=0 $ D2O sphere
7053  12 -0.0013   -7053 7058 7054 imp:n=1 imp:p,h,t,d,s=0 $ tube dans sphere
7054  12 -0.0013   -7054 imp:n=1 imp:p,h,t,d,s=0 $ bouchon dans tube
7055  12 -0.0013   -7055:-7056 imp:n=1 imp:p,h,t,d,s=0 $ bouchon sup
7057  12 -0.0013   -7057 7051 7053 7058 imp:n=1 imp:p,h,t,d,s=0 $ support inf
7058  12 -0.0013  -7058 7054 7029 #7030 7033 7034 &
    #7035 7037 #7039 imp:n=1 imp:p,h,t,d,s=0 $ air tube
7059  26 -7.700    -7059 7063 7051 imp:n=1 imp:p,h,t,d,s=0 $ support spr�re
7060  26 -7.700    -7060 7063 imp:n=1 imp:p,h,t,d,s=0 $ bride
7061  26 -7.700    -7061 7063 imp:n=1 imp:p,h,t,d,s=0 $ bride tube D=114.3 sup
7062  26 -7.700    -7062 7063 imp:n=1 imp:p,h,t,d,s=0 $ tube D=114.3
7063  12 -0.0013     -7063 7021 7027 7057 7029 7051 imp:n=1 imp:p,h,t,d,s=0 $ air tube D=114.3
7064  26 -7.700    (-7064:-7065) 7062 imp:n=1 imp:p,h,t,d,s=0 $ pattes tube D=114.3
7066  26 -7.700    -7066:-7067:-7068:-7069 imp:n=1 imp:p,h,t,d,s=0 $ pieds
c Cadmium sphere
7080  12 -0.0013   -7080 7051 7053 7059 imp:n=1 imp:p,h,t,d,s=0 $ Cadmium sphere
c Poutre sur ejection tube
7070  14 -7.8212   -7070 7071 7072 7073 7074 imp:n=1 imp:p,h,t,d,s=0 $ poutre
7071  12 -0.0013  -7071 7021 7072 7079 6122 6123 &
    6124 6125 #6049 imp:n=1 imp:p,h,t,d,s=0 $ air int poutre
7072  12 -0.0013     (-7072:-7073) 7021 imp:n=1 imp:p,h,t,d,s=0 $ passage ejection tube
7074  12 -0.0013     -7074 #6049 imp:n=1 imp:p,h,t,d,s=0 $ fente -X
7075  14 -7.8212   -7075 imp:n=1 imp:p,h,t,d,s=0 $ plaque +X
7076  14 -7.8212   -7076 7072 7073 imp:n=1 imp:p,h,t,d,s=0 $ plaque +Z
7077  14 -7.8212   -7077 7078 imp:n=1 imp:p,h,t,d,s=0 $ platine +Y
7078  12 -0.0013     -7078 imp:n=1 imp:p,h,t,d,s=0 $ air platine +Y
7079  14 -7.8212   -7079 imp:n=1 imp:p,h,t,d,s=0 $ platine inf
c chassis
7081  43 -1.7770   -7081 7082 imp:n=1 imp:p,h,t,d,s=0 $ chassis Bloc source
7082  12 -0.0013     -7082 7083 7005 imp:n=1 imp:p,h,t,d,s=0 $ air chassis Bloc source
7083  43 -1.7770   -7083 7005 imp:n=1 imp:p,h,t,d,s=0 $ renfort chassis Bloc source
7084  43 -1.7770   -7084:-7085:-7086:-7087 imp:n=1 imp:p,h,t,d,s=0 $ pieds bloc
7088  43 -1.9466   -7088 7089 imp:n=1 imp:p,h,t,d,s=0 $ support armoire elec
7089  12 -0.0013     -7089 imp:n=1 imp:p,h,t,d,s=0 $ air support armoire elec
7090  43 -1.9466   -7090:-7091:-7092:-7093 imp:n=1 imp:p,h,t,d,s=0 $ pieds
7094  38 -1.2000   -7094 imp:n=1 imp:p,h,t,d,s=0 $ armoire elec
7095  43 -1.7770   -7095:-7096:-7097:-7098 imp:n=1 imp:p,h,t,d,s=0 $ roues
C Stocked source Am-Be
C ----- suite aux informations non-disponibles, la source est celle du fichier Van_Gogh.i fourni -----
7101  24 -2.685    -7101 7019 imp:n=1 imp:p,h,t,d,s=0 $ piston Am-Be
7102  26 -7.700    -7102 imp:n=1 imp:p,h,t,d,s=0 $ tige support
7103  12 -0.0013     -7103 7102 imp:n=1 imp:p,h,t,d,s=0 $ esp. air/tige support
7104  33 -2.8      -7104 7103 imp:n=1 imp:p,h,t,d,s=0 $ partie inf.tube dural
7105  33 -2.8      -7105 7103 7114 imp:n=1 imp:p,h,t,d,s=0 $ capot tube dural
7108  12 -0.0013     -7108 7105 imp:n=1 imp:p,h,t,d,s=0 $ air capot tube dural
7109  26 -7.700    -7109 7110 imp:n=1 imp:p,h,t,d,s=0 $ support source
7110  26 -7.700    -7110 7111 imp:n=1 imp:p,h,t,d,s=0 $ capsule source
7111  21 -2.7882   -7111 imp:n=1 imp:p,h,t,d,s=0 $ zone active Am-Be
7112  26 -7.700    -7112 7109 7110 7113 imp:n=1 imp:p,h,t,d,s=0 $ capot maintien source
7113  12 -0.0013     -7113 7110 imp:n=1 imp:p,h,t,d,s=0 $ espace d'air
7114  12 -0.0013     -7114 7112 imp:n=1 imp:p,h,t,d,s=0 $ espace air sup. capot
7115  25 -11.35    -7115 7108 7105 7104 imp:n=1 imp:p,h,t,d,s=0 $ ecran plomb ep. 1mm
c ----- englobant sous poutre & poutre -----
7120   12   -0.0013  -7120 7095 7096 7097 7098 7081 7084 &
                        7085 7086 7087 7088 7090 7091 7092 &
                        7093 7094 7005 7001 7006 7023 7024 &
                        7025 7021                imp:n=1 imp:p,h,t,d,s=0 $ englobant sous poutre
7121  12 -0.0013  -7121 7070 7075 7076 7077 7021 &
    7066 7067 7068 7069 imp:n=1 imp:p,h,t,d,s=0 $ englobant poutre
C --- Detecteur-Berthold
100   1 -18.35     -100 -101 102 trcl=401      imp:n,h,t,d,s=1 imp:p=0
101   2 -0.001090816 -103 100 -101 102 trcl=401 imp:n,h,t,d,s=1 imp:p=0 $ density of (3.5 bars 3He + 1 bar CH4) - see 'Berthold_modelling_explanation_MENDEZ.msg'
102   3 -2.7       (-105 -102 104 ):(-103 -104 106 &
    ) trcl=401                                 imp:n,h,t,d,s=1 imp:p=0
103   3 -2.7       (-105 101 -107 ):(-103 107 -108 &
    ):(-110 108 -109 ) trcl=401                imp:n,h,t,d,s=1 imp:p=0
104   2 -0.001090816 -103 105 101 -107 trcl=401 imp:n,h,t,d,s=1 imp:p=0
105   2 -0.001090816 -103 105 104 -102 trcl=401 imp:n,h,t,d,s=1 imp:p=0
106   4 -7.86      103 -111 106 -108 trcl=401   imp:n,h,t,d,s=1 imp:p=0
107   5 -8.65      -115 114 112 -113 trcl=401 imp:n=1 imp:p,h,t,d,s=0
108   6 -0.001225  -121 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
109   6 -0.001225  -122 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
110   6 -0.001225  -123 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
111   6 -0.001225  -124 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
112   6 -0.001225  -125 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
113   6 -0.001225  -126 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
114   6 -0.001225  -127 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
115   6 -0.001225  -128 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
116   6 -0.001225  -129 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
117   6 -0.001225  -130 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
118   6 -0.001225  -131 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
119   6 -0.001225  -132 115 -133 trcl=401 imp:n=1 imp:p,h,t,d,s=0
120   8 -0.95      -133 #100 #101 #102 #103 #104 #105 &
    #106 #107 #122 #108 #109 #110 #111 #112 #113 #114 #115 &
    #116 #117 #118 #119 trcl=401 imp:n=1 imp:p,h,t,d,s=0
121   8 -0.95    -134 133 #122 #123 #124 #130 trcl=401 imp:n=1 imp:p,h,t,d,s=0
C --- Boitier
122   6 -0.001225  109 -117 -110 trcl=401 imp:n=1 imp:p,h,t,d,s=0
123   7 -7.8       (-115 119 117 -118 ):(-115 120 &
    118 -116 ) trcl=401 imp:n=1 imp:p,h,t,d,s=0
124   8 -0.95      (-119 110 117 -118 ):(-120 110 118 &
    -116 ) trcl=401 imp:n=1 imp:p,h,t,d,s=0
130   6 -0.001225  117 -116 -110 trcl=401 imp:n=1 imp:p,h,t,d,s=0 
C   
C 125   0            -135 #100 #101 #102 #103 #104 #105 &
C     #106 #107 #122 #123 #108 #109 #110 #111 #112 #113 #114 &
C     #115 #116 #117 #118 #119 #120 #124 #121 #130 u=126 imp:n=1 &
C     imp:p,h,t,d,s=0 $ near berthold exterior where imp = 1
C Englobant LB6411
C C126   0            -136 fill=126 imp:n=1 imp:p,h,t,d,s=0  trcl=401 $ englobant LB6411

C --------------------------------------------------------------------------- C
C -----                             SURFACES                            ----- C
C --------------------------------------------------------------------------- C
999   RPP  -1744.300   985.000  -1206.950   632.050   -330.000   950.000   $ Monde
C **************** C
C ***** HALL ***** C
C **************** C
5501  RPP  -1744.300   820.700   -641.950   632.050    -30.000     0.000   $ Dalle CEZANE
5502  RPP  -1744.300   820.700   -641.950   632.050   -330.000   -30.000   $ argile sous dalle
5503  RPP  -1739.300   815.700   -641.950   632.050      0.000   950.000   $ bardage ext Al
5504  RPP  -1739.200   815.600   -641.850   631.950      0.000   950.000   $ parol�ne
5505  RPP  -1734.400   810.800   -637.050   627.150      0.000   950.000   $ bardage int Al
5506  RPP  -1734.300   810.700   -636.950   627.050      0.000   950.000   $ Air Hall
5507  RPP  -1734.300   810.700   -641.950  -636.950    640.000   700.000   $ Fenetre -Y
5508  RPP  -1734.300   810.700    613.050   627.050    640.000   700.000   $ Fenetre +Y
5509  RPP  -1734.300   810.700   -636.950   613.050    904.000   909.200   $ toit bardage Al
5510  RPP  -1734.300   810.700   -636.950   613.050    904.100   909.100   $ toit parol�ne
5665  RPP  -1739.300 -1720.300   -299.950   290.050      0.000   400.000   $ air porte -X
5666  RPP    796.700   815.700   -299.950   290.050      0.000   400.000   $ air porte +X
5667  RPP  -1744.300 -1739.300   -304.950   295.050      0.000   400.000   $ bardage Al porte -X
5668  RPP  -1744.200 -1739.400   -304.850   294.950      0.100   399.900   $ bardage parol�ne porte -X
5669  RPP    815.700   820.700   -304.950   295.050      0.000   400.000   $ bardage Al porte +X
5670  RPP    815.800   820.600   -304.850   294.950      0.100   399.900   $ bardage parol�ne porte +X
C ----- Poutres U 140 -----                        
5511  RPP  -1734.300   810.700   -636.950  -622.950    153.500   160.000   $ -Y en 160
5512  RPP  -1734.300   810.700   -636.050  -623.850    153.500   159.500   $ -Y en 160
5513  RPP  -1734.300   810.700   -636.950  -622.950    313.500   320.000   $ -Y en 320
5514  RPP  -1734.300   810.700   -636.050  -623.850    313.500   319.500   $ -Y en 320
5515  RPP  -1734.300   810.700   -636.950  -622.950    473.500   480.000   $ -Y en 480
5516  RPP  -1734.300   810.700   -636.050  -623.850    473.500   479.500   $ -Y en 480
5517  RPP  -1734.300   810.700   -636.950  -622.950    633.500   640.000   $ -Y en 640
5518  RPP  -1734.300   810.700   -636.050  -623.850    633.500   639.500   $ -Y en 640
5519  RPP  -1734.300   810.700   -636.950  -622.950    700.000   706.500   $ -Y en 706.5
5520  RPP  -1734.300   810.700   -636.050  -623.850    700.500   706.500   $ -Y en 706.5
5521  RPP  -1734.300   810.700   -636.950  -622.950      0.000     6.500   $ -Y au sol
5522  RPP  -1734.300   810.700   -636.050  -623.850      0.000     6.000   $ -Y au sol
c                        
5523  RPP  -1734.300   810.700    613.050   627.050    153.500   160.000   $ +Y en 160
5524  RPP  -1734.300   810.700    613.950   626.150    153.500   159.500   $ +Y en 160
5525  RPP  -1734.300   810.700    613.050   627.050    313.500   320.000   $ +Y en 320
5526  RPP  -1734.300   810.700    613.950   626.150    313.500   319.500   $ +Y en 320
5527  RPP  -1734.300   810.700    613.050   627.050    473.500   480.000   $ +Y en 480
5528  RPP  -1734.300   810.700    613.950   626.150    473.500   479.500   $ +Y en 480
5529  RPP  -1734.300   810.700    613.050   627.050    633.500   640.000   $ +Y en 640
5530  RPP  -1734.300   810.700    613.950   626.150    633.500   639.500   $ +Y en 640
5531  RPP  -1734.300   810.700    613.050   627.050    700.000   706.500   $ +Y en 706.5
5532  RPP  -1734.300   810.700    613.950   626.150    700.500   706.500   $ +Y en 706.5
5533  RPP  -1734.300   810.700    613.050   627.050      0.000     6.500   $ +Y au sol
5534  RPP  -1734.300   810.700    613.950   626.150      0.000     6.000   $ +Y au sol
c                        
5535  RPP  -1734.300 -1720.300   -622.950   613.050    153.500   160.000   $ -X en 160
5536  RPP  -1733.400 -1721.200   -622.950   613.050    153.500   159.500   $ -X en 160
5537  RPP  -1734.300 -1720.300   -622.950   613.050    313.500   320.000   $ -X en 320
5538  RPP  -1733.400 -1721.200   -622.950   613.050    313.500   319.500   $ -X en 320
5539  RPP  -1734.300 -1720.300   -622.950   613.050    473.500   480.000   $ -X en 480
5540  RPP  -1733.400 -1721.200   -622.950   613.050    473.500   479.500   $ -X en 480
5541  RPP  -1734.300 -1720.300   -622.950   613.050    633.500   640.000   $ -X en 640
5542  RPP  -1733.400 -1721.200   -622.950   613.050    633.500   639.500   $ -X en 640
5543  RPP  -1734.300 -1720.300   -636.950   627.050    793.500   800.000   $ -X en 800
5544  RPP  -1733.400 -1721.200   -636.950   627.050    793.500   799.500   $ -X en 800
5545  RPP  -1734.300 -1720.300   -622.950   613.050      0.000     6.500   $ -X au sol
5546  RPP  -1733.400 -1721.200   -622.950   613.050      0.000     6.000   $ -X au sol
c                        
5547  RPP    796.700   810.700   -622.950   613.050    153.500   160.000   $ +X en 160
5548  RPP    797.600   809.800   -622.950   613.050    153.500   159.500   $ +X en 160
5549  RPP    796.700   810.700   -622.950   613.050    313.500   320.000   $ +X en 320
5550  RPP    797.600   809.800   -622.950   613.050    313.500   319.500   $ +X en 320
5551  RPP    796.700   810.700   -622.950   613.050    473.500   480.000   $ +X en 480
5552  RPP    797.600   809.800   -622.950   613.050    473.500   479.500   $ +X en 480
5553  RPP    796.700   810.700   -622.950   613.050    633.500   640.000   $ +X en 640
5554  RPP    797.600   809.800   -622.950   613.050    633.500   639.500   $ +X en 640
5555  RPP    796.700   810.700   -636.950   627.050    793.500   800.000   $ +X en 800
5556  RPP    797.600   809.800   -636.950   627.050    793.500   799.500   $ +X en 800
5557  RPP    796.700   810.700   -622.950   613.050      0.000     6.500   $ +X au sol
5558  RPP    797.600   809.800   -622.950   613.050      0.000     6.000   $ +X au sol
C ----- Poutres I 360 -----                        
5559  RPP  -1720.300 -1703.300   -622.950   -586.950     0.000   854.000   $ -Y_1
5560  RPP  -1720.300 -1712.200   -621.680   -588.220     0.000   854.000   $ -Y_1
5561  RPP  -1711.400 -1703.300   -621.680   -588.220     0.000   854.000   $ -Y_1
5562  RPP  -1220.300 -1203.300   -622.950   -586.950     0.000   854.000   $ -Y_2
5563  RPP  -1220.300 -1212.200   -621.680   -588.220     0.000   854.000   $ -Y_2
5564  RPP  -1211.400 -1203.300   -621.680   -588.220     0.000   854.000   $ -Y_2
5565  RPP   -720.300  -703.300   -622.950   -586.950     0.000   854.000   $ -Y_3
5566  RPP   -720.300  -712.200   -621.680   -588.220     0.000   854.000   $ -Y_3
5567  RPP   -711.400  -703.300   -621.680   -588.220     0.000   854.000   $ -Y_3
5568  RPP   -220.300  -203.300   -622.950   -586.950     0.000   854.000   $ -Y_4
5569  RPP   -220.300  -212.200   -621.680   -588.220     0.000   854.000   $ -Y_4
5570  RPP   -211.400  -203.300   -621.680   -588.220     0.000   854.000   $ -Y_4
5571  RPP    279.700   296.700   -622.950   -586.950     0.000   854.000   $ -Y_5
5572  RPP    279.700   287.800   -621.680   -588.220     0.000   854.000   $ -Y_5
5573  RPP    288.600   296.700   -621.680   -588.220     0.000   854.000   $ -Y_5
5574  RPP    779.700   796.700   -622.950   -586.950     0.000   854.000   $ -Y_6
5575  RPP    779.700   787.800   -621.680   -588.220     0.000   854.000   $ -Y_6
5576  RPP    788.600   796.700   -621.680   -588.220     0.000   854.000   $ -Y_6
c                        
5577  RPP  -1720.300 -1703.300    577.050    613.050     0.000   854.000   $ +Y_1
5578  RPP  -1720.300 -1712.200    578.320    611.780     0.000   854.000   $ +Y_1
5579  RPP  -1711.400 -1703.300    578.320    611.780     0.000   854.000   $ +Y_1
5580  RPP  -1220.300 -1203.300    577.050    613.050     0.000   854.000   $ +Y_2
5581  RPP  -1220.300 -1212.200    578.320    611.780     0.000   854.000   $ +Y_2
5582  RPP  -1211.400 -1203.300    578.320    611.780     0.000   854.000   $ +Y_2
5583  RPP   -720.300  -703.300    577.050    613.050     0.000   854.000   $ +Y_3
5584  RPP   -720.300  -712.200    578.320    611.780     0.000   854.000   $ +Y_3
5585  RPP   -711.400  -703.300    578.320    611.780     0.000   854.000   $ +Y_3
5586  RPP   -220.300  -203.300    577.050    613.050     0.000   854.000   $ +Y_4
5587  RPP   -220.300  -212.200    578.320    611.780     0.000   854.000   $ +Y_4
5588  RPP   -211.400  -203.300    578.320    611.780     0.000   854.000   $ +Y_4
5589  RPP    279.700   296.700    577.050    613.050     0.000   854.000   $ +Y_5
5590  RPP    279.700   287.800    578.320    611.780     0.000   854.000   $ +Y_5
5591  RPP    288.600   296.700    578.320    611.780     0.000   854.000   $ +Y_5
5592  RPP    779.700   796.700    577.050    613.050     0.000   854.000   $ +Y_6
5593  RPP    779.700   787.800    578.320    611.780     0.000   854.000   $ +Y_6
5594  RPP    788.600   796.700    578.320    611.780     0.000   854.000   $ +Y_6
c                        
5595  RPP  -1720.300 -1703.300   -622.950    613.050   854.000   890.000   $ +Z_1
5596  RPP  -1720.300 -1712.200   -622.950    613.050   855.270   888.730   $ +Z_1
5597  RPP  -1711.400 -1703.300   -622.950    613.050   855.270   888.730   $ +Z_1
5598  RPP  -1220.300 -1203.300   -622.950    613.050   854.000   890.000   $ +Z_2
5599  RPP  -1220.300 -1212.200   -622.950    613.050   855.270   888.730   $ +Z_2
5600  RPP  -1211.400 -1203.300   -622.950    613.050   855.270   888.730   $ +Z_2
5601  RPP   -720.300  -703.300   -622.950    613.050   854.000   890.000   $ +Z_3
5602  RPP   -720.300  -712.200   -622.950    613.050   855.270   888.730   $ +Z_3
5603  RPP   -711.400  -703.300   -622.950    613.050   855.270   888.730   $ +Z_3
5604  RPP   -220.300  -203.300   -622.950    613.050   854.000   890.000   $ +Z_4
5605  RPP   -220.300  -212.200   -622.950    613.050   855.270   888.730   $ +Z_4
5606  RPP   -211.400  -203.300   -622.950    613.050   855.270   888.730   $ +Z_4
5607  RPP    279.700   296.700   -622.950    613.050   854.000   890.000   $ +Z_5
5608  RPP    279.700   287.800   -622.950    613.050   855.270   888.730   $ +Z_5
5609  RPP    288.600   296.700   -622.950    613.050   855.270   888.730   $ +Z_5
5610  RPP    779.700   796.700   -622.950    613.050   854.000   890.000   $ +Z_6
5611  RPP    779.700   787.800   -622.950    613.050   855.270   888.730   $ +Z_6
5612  RPP    788.600   796.700   -622.950    613.050   855.270   888.730   $ +Z_6
C ----- Poutres I 300 -----                        
5613  RPP  -1720.300 -1690.300   -314.950   -299.950     0.000   854.000   $ -X_1
5614  RPP  -1719.230 -1691.370   -314.950   -307.805     0.000   854.000   $ -X_1
5615  RPP  -1719.230 -1691.370   -307.095   -299.950     0.000   854.000   $ -X_1
5616  RPP  -1720.300 -1690.300    -12.450      2.550   410.000   854.000   $ -X_2
5617  RPP  -1719.230 -1691.370    -12.450     -5.305   410.000   854.000   $ -X_2
5618  RPP  -1719.230 -1691.370     -4.595      2.550   410.000   854.000   $ -X_2
5619  RPP  -1720.300 -1690.300    290.050    305.050     0.000   854.000   $ -X_3
5620  RPP  -1719.230 -1691.370    290.050    297.195     0.000   854.000   $ -X_3
5621  RPP  -1719.230 -1691.370    297.905    305.050     0.000   854.000   $ -X_3
5622  RPP    766.700   796.700   -314.950   -299.950     0.000   854.000   $ +X_1
5623  RPP    767.770   795.630   -314.950   -307.805     0.000   854.000   $ +X_1
5624  RPP    767.770   795.630   -307.095   -299.950     0.000   854.000   $ +X_1
5625  RPP    766.700   796.700    -12.450      2.550   410.000   854.000   $ +X_2
5626  RPP    767.770   795.630    -12.450     -5.305   410.000   854.000   $ +X_2
5627  RPP    767.770   795.630     -4.595      2.550   410.000   854.000   $ +X_2
5628  RPP    766.700   796.700    290.050    305.050     0.000   854.000   $ +X_3
5629  RPP    767.770   795.630    290.050    297.195     0.000   854.000   $ +X_3
5630  RPP    767.770   795.630    297.905    305.050     0.000   854.000   $ +X_3
C ----- Poutres U 300 (portes) -----                        
5631  RPP  -1720.300 -1690.300   -299.950    290.050   400.000   410.000   $ -X porte
5632  RPP  -1719.800 -1691.800   -299.950    290.050   400.000   409.050   $ -X porte
5633  RPP    766.700   796.700   -299.950    290.050   400.000   410.000   $ +X porte
5634  RPP    768.200   795.200   -299.950    290.050   400.000   409.050   $ +X porte
C ----- Poutres I 140 (toit) -----                        
5635  RPP  -1734.300   810.700   -586.950   -579.650   890.000   904.000   $ +Z_1
5636  RPP  -1734.300   810.700   -586.950   -583.535   890.690   903.310   $ +Z_1
5637  RPP  -1734.300   810.700   -583.065   -579.650   890.690   903.310   $ +Z_1
5638  RPP  -1734.300   810.700   -311.100   -303.800   890.000   904.000   $ +Z_2
5639  RPP  -1734.300   810.700   -311.100   -307.685   890.690   903.310   $ +Z_2
5640  RPP  -1734.300   810.700   -307.215   -303.800   890.690   903.310   $ +Z_2
5641  RPP  -1734.300   810.700    -19.750    -12.450   890.000   904.000   $ +Z_3
5642  RPP  -1734.300   810.700    -19.750    -16.335   890.690   903.310   $ +Z_3
5643  RPP  -1734.300   810.700    -15.865    -12.450   890.690   903.310   $ +Z_3
5644  RPP  -1734.300   810.700      2.550      9.850   890.000   904.000   $ +Z_4
5645  RPP  -1734.300   810.700      2.550      5.965   890.690   903.310   $ +Z_4
5646  RPP  -1734.300   810.700      6.435      9.850   890.690   903.310   $ +Z_4
5647  RPP  -1734.300   810.700    293.900    301.200   890.000   904.000   $ +Z_5
5648  RPP  -1734.300   810.700    293.900    297.315   890.690   903.310   $ +Z_5
5649  RPP  -1734.300   810.700    297.785    301.200   890.690   903.310   $ +Z_5
5650  RPP  -1734.300   810.700    605.750    613.050   890.000   904.000   $ +Z_6
5651  RPP  -1734.300   810.700    605.750    609.165   890.690   903.310   $ +Z_6
5652  RPP  -1734.300   810.700    609.635    613.050   890.690   903.310   $ +Z_6
C ----- Rails -----                        
5653  RPP  -1734.300   810.700   -566.550   -557.350   700.000   701.100   $ -Y
5654  RPP  -1734.300   810.700   -562.450   -561.450   701.100   707.100   $ -Y
5655  RPP  -1734.300   810.700   -564.450   -559.450   707.100   710.000   $ -Y
5656  RPP  -1734.300   810.700    547.450    556.650   700.000   701.100   $ +Y
5657  RPP  -1734.300   810.700    551.550    552.550   701.100   707.100   $ +Y
5658  RPP  -1734.300   810.700    549.550    554.550   707.100   710.000   $ +Y
C ----- PontRoulant -----                        
5661  RPP  -1690.300 -1665.300   -564.450    554.550   710.000   766.000   $ Poutre_1
5662  RPP  -1688.600 -1667.000   -564.450    554.550   711.700   764.300   $ Poutre_1
5663  RPP  -1551.300 -1526.300   -564.450    554.550   710.000   766.000   $ Poutre_2
5664  RPP  -1549.600 -1528.000   -564.450    554.550   711.700   764.300   $ Poutre_2
c ----- Caniveaux -----                        
5681  RPP  -1666.700   333.300   -531.650   -457.650   -65.000     0.000   $ air Caniveau -X
5682  RPP  -1681.700   348.300   -546.650   -442.650   -80.000   -30.000   $ Caniveau -X
5683  RPP  -1220.700 -1166.700   -457.650     42.350   -65.000     0.000   $ air Caniveau Y1
5684  RPP  -1235.700 -1151.700   -442.650     58.350   -80.000   -30.000   $ Caniveau Y1
5685  RPP   -720.700  -666.700   -457.650    -37.650   -65.000     0.000   $ air Caniveau Y2
5686  RPP   -735.700  -651.700   -442.650    -21.650   -80.000   -30.000   $ Caniveau Y2
5687  RPP   -310.700  -256.700   -457.650     42.350   -65.000     0.000   $ air Caniveau Y3
5688  RPP   -325.700  -241.700   -442.650     58.350   -80.000   -30.000   $ Caniveau Y3
5689  RPP    279.300   333.300   -457.650     42.350   -65.000     0.000   $ air Caniveau Y4
5690  RPP    264.300   348.300   -442.650     58.350   -80.000   -30.000   $ Caniveau Y4
c ----- plaques acier et cables -----                        
5691  RPP  -1666.700   333.300   -531.650   -457.650    -1.000     0.000   $ Plaque -X
5692  RPP  -1666.700   333.300   -514.650   -474.650   -65.000   -25.000   $ Cables 40x40 -X
5693  RPP  -1220.700 -1166.700   -457.650     42.350    -1.000     0.000   $ Plaque Y1
5694  RPP  -1208.700 -1178.700   -474.650     42.350   -65.000   -35.000   $ Cables 30x30  Y1
5695  RPP   -720.700  -666.700   -457.650    -37.650    -1.000     0.000   $ Plaque Y2
5696  RPP   -708.700  -678.700   -474.650    -37.650   -65.000   -35.000   $ Cables 30x30  Y2
5697  RPP   -310.700  -256.700   -457.650     42.350    -1.000     0.000   $ Plaque Y3
5698  RPP   -298.700  -268.700   -474.650     42.350   -65.000   -35.000   $ Cables 30x30  Y3
5699  RPP    279.300   333.300   -457.650     42.350    -1.000     0.000   $ Plaque Y4
5700  RPP    291.300   321.300   -474.650     42.350   -65.000   -35.000   $ Cables 30x30  Y4
c ----- Escalier -----                        
5701  RPP  -1341.700 -1321.700   -442.650   -352.650   -56.000   -16.000   $ marche 01
5702  RPP  -1361.700 -1341.700   -442.650   -352.650   -76.000   -36.000   $ marche 02
5703  RPP  -1381.700 -1361.700   -442.650   -352.650   -96.000   -56.000   $ marche 03
5704  RPP  -1401.700 -1381.700   -442.650   -352.650  -116.000   -76.000   $ marche 04
5705  RPP  -1421.700 -1401.700   -442.650   -352.650  -136.000   -96.000   $ marche 05
5706  RPP  -1441.700 -1421.700   -442.650   -352.650  -156.000  -116.000   $ marche 06
5707  RPP  -1461.700 -1441.700   -442.650   -352.650  -176.000  -136.000   $ marche 07
5708  RPP  -1481.700 -1461.700   -442.650   -352.650  -196.000  -156.000   $ marche 08
5709  RPP  -1501.700 -1481.700   -442.650   -352.650  -216.000  -176.000   $ marche 09
5710  RPP  -1521.700 -1501.700   -442.650   -352.650  -236.000  -196.000   $ marche 10
5711  RPP  -1541.700 -1521.700   -442.650   -352.650  -256.000  -216.000   $ marche 11
5712  RPP  -1561.700 -1541.700   -442.650   -352.650  -276.000  -236.000   $ marche 12
5713  RPP  -1581.700 -1561.700   -442.650   -352.650  -296.000  -256.000   $ marche 13
5714  RPP  -1601.700 -1581.700   -442.650   -352.650  -316.000  -276.000   $ marche 14
5715  RPP  -1621.700 -1601.700   -442.650   -352.650  -316.000  -296.000   $ marche 15
5716  RPP  -1666.700 -1321.700   -442.650   -352.650   -16.000     0.000   $ air escalier
5717  RPP  -1461.700 -1341.700   -442.650   -352.650   -76.000   -16.000   
5718  RPP  -1666.700 -1461.700   -442.650   -352.650  -156.000   -16.000   
5719  RPP  -1461.700 -1401.700   -442.650   -352.650  -136.000   -76.000   
5720  RPP  -1521.700 -1481.700   -442.650   -352.650  -196.000  -156.000   
5721  RPP  -1581.700 -1521.700   -442.650   -352.650  -256.000  -156.000   
5722  RPP  -1666.700 -1581.700   -442.650   -352.650  -316.000  -156.000   
c ----- Garde-Corps -----                        
5723  RPP  -1666.700 -1662.700   -446.650   -442.650     0.000    92.000   $ poteau -X-Y
5724  RPP  -1666.500 -1662.900   -446.450   -442.850     0.000    92.000   $ air poteau -X-Y
5725  RPP  -1325.700 -1321.700   -446.650   -442.650     0.000    92.000   $ poteau +X-Y
5726  RPP  -1325.500 -1321.900   -446.450   -442.850     0.000    92.000   $ air poteau +X-Y
5727  RPP  -1666.700 -1662.700   -352.650   -348.650     0.000    92.000   $ poteau -X+Y
5728  RPP  -1666.500 -1662.900   -352.450   -348.850     0.000    92.000   $ air poteau -X+Y
5729  RPP  -1325.700 -1321.700   -352.650   -348.650     0.000    92.000   $ poteau +X+Y
5730  RPP  -1325.500 -1321.900   -352.450   -348.850     0.000    92.000   $ air poteau +X+Y
5731  RPP  -1553.700 -1549.700   -446.650   -442.650     0.000    92.000   $ poteaux -Y
5732  RPP  -1553.500 -1549.900   -446.450   -442.850     0.000    92.000   
5733  RPP  -1438.700 -1434.700   -446.650   -442.650     0.000    92.000   
5734  RPP  -1438.500 -1434.900   -446.450   -442.850     0.000    92.000   
5735  RPP  -1553.700 -1549.700   -352.650   -348.650     0.000    92.000   $ poteau +Y
5736  RPP  -1553.500 -1549.900   -352.450   -348.850     0.000    92.000   
5737  RPP  -1438.700 -1434.700   -352.650   -348.650     0.000    92.000   
5738  RPP  -1438.500 -1434.900   -352.450   -348.850     0.000    92.000   
5739  RPP  -1662.700 -1325.700   -446.650   -442.650    36.000    40.000   $ barre -Y
5740  RPP  -1662.700 -1325.700   -446.450   -442.850    36.200    39.800   
5741  RPP  -1662.700 -1325.700   -352.650   -348.650    36.000    40.000   $ barre +Y
5742  RPP  -1662.700 -1325.700   -352.450   -348.850    36.200    39.800   
5743  RPP  -1666.700 -1662.700   -442.650   -352.650    36.000    40.000   $ barre -X
5744  RPP  -1666.500 -1662.900   -442.650   -352.650    36.200    39.800   
5745  RPP  -1666.700 -1321.700   -446.650   -442.650    92.000   100.000   $ barres +Z
5746  RPP  -1666.500 -1321.900   -446.450   -442.850    92.200    99.800   
5747  RPP  -1666.700 -1321.700   -352.650   -348.650    92.000   100.000   
5748  RPP  -1666.500 -1321.900   -352.450   -348.850    92.200    99.800   
5749  RPP  -1666.700 -1662.700   -442.650   -352.650    92.000   100.000   
5750  RPP  -1666.500 -1662.900   -442.650   -352.650    92.200    99.800   
c ----- Encombrement -----                        
6901  RPP   -183.300    -3.300   -622.950   -592.950    73.000   139.000   $ Bloc 1 Armoires elec.
6902  RPP   -425.300  -385.300   -622.950   -562.950     0.000    80.000   $ Bloc 2 Compresseur jaune
6903  RCC   -480.300  -607.950      0.000      0   0   125.000    15.000   $ Bloc 2 ballon
6904  RPP   -825.300  -775.300   -622.950   -602.950   110.000   160.000   $ Bloc 3 Armoir elec.
6905  RPP   -770.300  -720.300   -622.950   -582.950     0.000    50.000   $ Bloc 3 mini-compresseur
6906  RPP   -957.300  -837.300   -601.950   -541.950     0.000    80.000   $ Bloc 3 Comresseur bleu
6907  RCC   -992.300  -607.950      0.000      0   0   125.000    15.000   $ Bloc 3 ballon
6908  RPP  -1199.300 -1109.300   -622.950   -582.950     0.000   178.000   $ Bloc 4 Armore grise
6909  RPP  -1404.300 -1224.300   -622.950   -582.950     0.000   178.000   $ Bloc 4 Deux Armores grises
6910  RPP  -1554.300 -1464.300   -622.950   -592.950    78.000   178.000   $ Bloc 4 Armoir elec.
6911  RPP  -1720.300 -1690.300   -576.950   -416.950    98.000   178.000   $ Bloc 4 Deux Armores elec
6912  RPP  -1720.300 -1695.300   -576.950   -536.950    38.000    78.000   $ Bloc 4 Armoir elec.
6913  RPP   -797.300  -737.300    280.050    310.050    50.000   144.000   $ Bloc 5 Armoir elec. T400
6914  RPP   -792.300  -742.300    280.050    305.050     0.000    50.000   
6915  RPP   -592.300  -514.300     96.050    136.050     0.000   170.000   $ Bloc 6 Armoires elec. Van Gogh
6916  RPP   -652.300  -592.300     96.050    124.050     0.000    80.000   
6917  RPP   -686.300  -648.300    -83.950    -20.950    87.000   170.000   $ Bloc 7 Armoires elec. sous Van Gogh
6918  RPP   -625.300  -570.300     55.050     81.050   116.000   160.000   
6919  RPP   -346.500  -281.500   -253.950   -173.950   111.000   191.000   $ Bloc 8 Armoires elec. sous Van Gogh
6920  RPP   -346.500  -313.500   -121.950    -77.950    81.000   191.000   
6921  RPP   -196.300  -116.300    -23.950     41.050    90.000   170.000   
6922  RPP    290.700   340.700    197.050    447.050     0.000   150.000   $ Muret local source
6923  RPP    340.700   540.700    197.050    247.050     0.000   150.000   
6924  RPP    540.700   590.700    197.050    247.050     0.000   100.000   
6925  RPP    490.700   570.700    563.050    613.050     0.000   200.000   $ Armoires local source
6926  RPP    345.700   415.700    443.050    503.050     0.000   100.000   
6927  RPP    415.000   810.700   -636.950   -296.350     0.000   263.500   $ Local B�G
6928  RPP    415.100   810.700   -636.950   -296.450     0.000   263.400   
6929  RPP    419.900   810.700   -636.950   -301.250     0.000   258.600   
6930  RPP    420.000   810.700   -636.950   -301.350     0.000   258.500   
6931  RPP    290.700   390.700   -571.950   -321.950     0.000    50.000   $ Ventilation devant local BaG
6932  RCC  -1489.300   345.750      0.000      0   0   250.000    47.750   $ Ballon T400
6933  RCC  -1489.300   345.750      1.000      0   0   248.000    46.750   
6934  RPP  -1259.300 -1254.300    245.750    445.750     0.000     5.000   $ Support en T
6935  RPP  -1356.800 -1156.800    343.250    348.250     0.000     5.000   
6936  RCC  -1256.800   345.750      5.000      0   0   225.000     8.415   $ Tube vertical
6937  RCC  -1256.800   345.750      5.000      0   0   225.000     8.015   
6938  RCC  -1304.800   345.750    230.000    100.000     0   0     8.415   $ Gros tube horizontal
6939  RCC  -1304.400   345.750    230.000     99.200     0   0     8.015   
6940  RCC  -1342.800   345.750    230.000    238.000     0   0     6.670   $ Petit tube horizontal
6941  RCC  -1342.800   345.750    230.000    238.000     0   0     6.270   
6942  RCC  -1124.800   345.750    230.000     20.000     0   0    23.000   $ Soufflet 2 mm �paisseur
6943  RCC  -1124.600   345.750    230.000     19.600     0   0    22.800   
c ----- Air hors et zones travail -----                        
6944  RPP  -1734.300   810.700   -636.950    627.050     0.000   950.000   $ Air hors zone travail
6945  RPP  -1390.000   260.000   -290.000    150.000     0.000   203.500   $ Air zone travail VAN GOGN -Z 203.5
6946  RPP  -1390.000   260.000   -290.000    150.000   203.500   500.000   $ Air zone travail VAN GOGN +Z 203.5
6947  RPP  -1390.000   260.000    150.000    530.000     0.000   500.000   $ Air zone travail T400
6948  RPP   -650.550  -244.700    278.875    412.625   125.300   295.000   $ Air zone travail T400 - Banc
c ----- Local D�chets -----
6949  RPP    285.000   815.700   -706.950   -641.950     0.000   263.500   $ Bardage ext couloir
6950  RPP    285.100   815.600   -706.950   -641.950     0.000   263.400   $ Polypropyl�ne couloir
6951  RPP    289.900   810.800   -706.950   -641.950     0.000   258.600   $ Bardage int couloir
6952  RPP    290.000   810.700   -706.950   -641.950     0.000   258.500   $ Air couloir
6953  RPP    285.000   985.000  -1206.950   -706.950     0.000   263.500   $ Bardage ext local
6954  RPP    285.100   984.900  -1206.850   -707.050     0.000   263.400   $ Polypropyl�ne local
6955  RPP    289.900   980.100  -1202.050   -711.850     0.000   258.600   $ Bardage int local
6956  RPP    290.000   980.000  -1201.950   -711.950     0.000   258.500   $ Air local
6957  RPP    285.000   985.000  -1206.950   -641.950   -30.000     0.000   $ Dalle
6958  RPP    285.000   985.000  -1206.950   -641.950  -330.000   -30.000   $ Argile
C ******************************* C
C ***** PLATEFORME VAN GOGH ***** C
C ******************************* C
c ----- Structure -----                        
5751  RPP  -1037.500  -637.500   -163.750    -35.750   203.500   210.500   $ Sructure A
5752  RPP  -1034.000  -641.000   -160.250    -39.250   203.500   210.500   
5753  RPP  -1037.500  -957.500    -35.750     61.750   203.500   210.500   $ Sructure B
5754  RPP  -1034.000  -961.000    -32.250     58.250   203.500   210.500   
5755  RPP  -1037.500  -601.000     61.750    121.750   203.500   210.500   $ Sructure C
5756  RPP  -1034.000  -604.500     65.250    118.250   203.500   210.500   
5757  RPP   -601.000  -313.500     61.750    121.750   203.500   210.500   $ Sructure D
5758  RPP   -597.500  -317.000     65.250    118.250   203.500   210.500   
5759  RPP   -313.500   -55.500     25.250    121.750   203.500   210.500   $ Sructure E
5760  RPP   -310.000   -59.000     28.750    118.250   203.500   210.500   
5761  RPP    -82.500    93.500     25.250     55.650   173.500   180.500   $ Sructure F
5762  RPP    -79.000    90.000     28.750     52.150   173.500   180.500   
5763  RPP     66.500   147.500     25.250    121.750   203.500   210.500   $ Sructure G
5764  RPP     70.000   144.000     28.750    118.250   203.500   210.500   
5765  RPP   -617.500  -312.500   -163.750    -67.250   203.500   210.500   $ Sructure H
5766  RPP   -614.000  -316.000   -160.250    -70.750   203.500   210.500   
5767  RPP   -312.500  -217.500   -163.750    -20.750   203.500   210.500   $ Sructure I
5768  RPP   -309.000  -221.000   -160.250    -24.250   203.500   210.500   
5769  RPP   -217.500    57.600   -115.750    -20.750   203.500   210.500   $ Sructure J
5770  RPP   -217.500    54.100   -112.250    -24.250   203.500   210.500   
5771  RPP     57.600   152.500   -115.750    -20.750   203.500   210.500   $ Sructure K
5772  RPP     61.100   149.000   -112.250    -24.250   203.500   210.500   
5773  RPP    152.500   247.500   -115.750     44.250   203.500   210.500   $ Sructure L
5774  RPP    152.500   244.000   -112.250     40.750   203.500   210.500   
5775  RPP    152.500   156.000    -24.250     40.750   203.500   210.500   $ Structure -X suppl.
5776  RPP    152.800   155.700    -23.950     40.750   203.800   210.200   
c ----- Caillebotis -----                           
5781  RPP  -1037.500  -637.500   -163.750    -35.750   210.500   213.500   $ Caillebotie A
5782  RPP  -1037.500  -957.500    -35.750     61.750   210.500   213.500   $ Caillebotie B
5783  RPP  -1037.500  -601.000     61.750    121.750   210.500   213.500   $ Caillebotie C
5784  RPP   -601.000  -313.500     61.750    121.750   210.500   213.500   $ Caillebotie D
5785  RPP   -313.500   -55.500     25.250    121.750   210.500   213.500   $ Caillebotie E
5786  RPP    -82.500    93.500     25.250     55.650   180.500   183.500   $ Caillebotie F
5787  RPP     66.500   147.500     25.250    121.750   210.500   213.500   $ Caillebotie G
5788  RPP   -617.500  -312.500   -163.750    -67.250   210.500   213.500   $ Caillebotie H
5789  RPP   -312.500  -217.500   -163.750    -20.750   210.500   213.500   $ Caillebotie I
5790  RPP   -217.500    57.600   -115.750    -20.750   210.500   213.500   $ Caillebotie J
5791  RPP     57.600   152.500   -115.750    -20.750   210.500   213.500   $ Caillebotie K
5792  RPP    152.500   247.500   -115.750     44.250   210.500   213.500   $ Caillebotie L
c ----- Renforts structure + pied                               
5795  RPP  -1011.500 -1005.500   -160.250    -39.250   204.500   210.500   $ Pieds P5_A
5796  RPP  -1011.500 -1005.500   -160.250   -154.250     0.000   204.500   
5797  RPP  -1011.500 -1005.500    -45.250    -39.250     0.000   204.500   
5798  RPP  -1011.500 -1005.500   -154.250    -45.250   100.000   106.000   
5799  RPP   -933.500  -930.000   -160.250    -39.250   203.500   210.500   $ Renfort A
5800  RPP   -829.500  -823.500   -160.250    -39.250   204.500   210.500   $ Pieds P6_A
5801  RPP   -829.500  -823.500   -160.250   -154.250     0.000   204.500   
5802  RPP   -829.500  -823.500    -95.250    -89.250     0.000   204.500   
5803  RPP   -829.500  -823.500   -154.250    -95.250   100.000   106.000   
5804  RPP   -737.500  -734.000   -160.250    -39.250   203.500   210.500   $ Renfort A
5805  RPP   -647.500  -641.500   -160.250    -39.250   204.500   210.500   $ Pieds P7_A
5806  RPP   -647.500  -641.500   -160.250   -154.250     0.000   204.500   
5807  RPP   -647.500  -641.500    -45.250    -39.250     0.000   204.500   
5808  RPP   -647.500  -641.500   -154.250    -45.250   100.000   106.000   
5809  RPP  -1033.200 -1027.200     65.250    118.250   204.500   210.500   $ Pieds P2_C
5810  RPP  -1033.200 -1027.200    112.250    118.250     0.000   204.500   
5811  RPP   -901.000  -895.000     65.250    118.250   204.500   210.500   $ Pieds P1_C
5812  RPP   -901.000  -895.000     88.750     94.750     0.000   204.500   
5813  RPP   -743.000  -737.000     65.250    118.250   204.500   210.500   $ Pieds P1_C
5814  RPP   -743.000  -737.000     88.750     94.750     0.000   204.500   
5815  RPP   -624.000  -618.000     65.250    118.250   204.500   210.500   $ Pieds P1_C
5816  RPP   -624.000  -618.000     88.750     94.750     0.000   204.500   
5817  RPP   -521.000  -515.000     65.250    118.250   204.500   210.500   $ Pieds P1_D
5818  RPP   -521.000  -515.000     88.750     94.750     0.000   204.500   
5819  RPP   -381.500  -375.500     65.250    118.250   204.500   210.500   $ Pieds P1_D
5820  RPP   -381.500  -375.500     88.750     94.750     0.000   204.500   
5821  RPP   -291.500  -285.500     28.750    118.250   204.500   210.500   $ Pieds P3_E
5822  RPP   -291.500  -285.500     55.250     61.250     0.000   204.500   
5823  RPP   -291.500  -285.500    112.250    118.250     0.000   204.500   
5824  RPP   -291.500  -285.500     61.250    112.250   100.000   106.000   
5825  RPP   -187.000  -183.500     28.750    118.250   203.500   210.500   $ Renfort E
5826  RPP    -85.500   -79.500     28.750    118.250   204.500   210.500   $ Pieds P4_E
5827  RPP    -85.500   -79.500     55.650     61.650     0.000   204.500   
5828  RPP    -85.500   -79.500    112.250    118.250     0.000   204.500   
5829  RPP    -85.500   -79.500     61.650    112.250   100.000   106.000   
5830  RPP    -62.500   -59.000     28.750     52.150   173.500   180.500   $ Renfort F
5831  RPP      3.500     7.000     28.750     52.150   173.500   180.500   
5832  RPP     70.000    73.500     28.750     52.150   173.500   180.500   
5833  RPP    117.500   123.500     28.750    118.250   204.500   210.500   $ Pieds P4_G
5834  RPP    117.500   123.500     55.250     61.250     0.000   204.500   
5835  RPP    117.500   123.500    112.250    118.250     0.000   204.500   
5836  RPP    117.500   123.500     61.250    112.250   100.000   106.000   
5837  RPP     80.500    86.500     28.750    118.250   204.500   210.500   $ Pieds P3_G
5838  RPP     80.500    86.500     55.650     61.650     0.000   204.500   
5839  RPP     80.500    86.500    112.250    118.250     0.000   204.500   
5840  RPP     80.500    86.500     61.650    112.250   100.000   106.000   
5841  RPP   -585.500  -579.500   -160.250    -70.750   204.500   210.500   $ Pieds PX_H
5842  RPP   -585.500  -579.500   -160.250   -154.250     0.000   204.500   
5843  RPP   -585.500  -579.500    -76.750    -70.750     0.000   204.500   
5844  RPP   -585.500  -579.500   -154.250    -76.750   100.000   106.000   
5845  RPP   -352.500  -346.500   -160.250    -70.750   204.500   210.500   $ Pieds PX_H
5846  RPP   -352.500  -346.500   -160.250   -154.250     0.000   204.500   
5847  RPP   -352.500  -346.500    -76.750    -70.750     0.000   204.500   
5848  RPP   -352.500  -346.500   -154.250    -76.750   100.000   106.000   
5849  RPP   -207.500  -201.500   -112.250    -24.250   204.500   210.500   $ Pieds PX_J
5850  RPP   -207.500  -201.500   -112.250   -106.250     0.000   204.500   
5851  RPP   -207.500  -201.500    -30.250    -24.250     0.000   204.500   
5852  RPP   -207.500  -201.500   -106.250    -30.250   100.000   106.000   
5853  RPP    -50.300   -44.300   -112.250    -24.250   204.500   210.500   $ Pieds PX_J
5854  RPP    -50.300   -44.300   -112.250   -106.250     0.000   204.500   
5855  RPP    -50.300   -44.300    -30.250    -24.250    50.000   204.500   
5856  RPP    -50.300   -44.300   -106.250    -30.250   100.000   106.000   
5857  RPP    143.000   149.000   -112.250    -24.250   204.500   210.500   $ Pieds PX_K
5858  RPP    143.000   149.000   -112.250   -106.250     0.000   204.500   
5859  RPP    143.000   149.000    -30.250    -24.250     0.000   204.500   
5860  RPP    143.000   149.000   -106.250    -30.250   100.000   106.000   
5861  RPP    237.200   243.200    -88.750    -82.750     0.000   210.500   $ Pieds PX_L
5862  RPP    156.000   244.000      4.950     10.950   204.500   210.500   $ Pieds PX_L
5863  RPP    156.000   162.000      4.950     10.950     0.000   204.500   
5864  RPP    238.000   244.000      4.950     10.950     0.000   204.500   
5865  RPP    162.000   238.000      4.950     10.950   100.000   106.000   
c ----- Garde-corps -----                           
5866  RPP  -1037.659  -448.500   -163.909   -163.750   203.500   321.000   $ Garde-Corps
5867  RPP  -1037.659 -1037.500   -163.750    121.750   203.500   321.000   
5868  RPP  -1037.659   -55.500    121.750    121.909   203.500   321.000   
5869  RPP     66.500   147.659    121.750    121.909   203.500   321.000   
5870  RPP    147.500   147.659     44.409    121.750   203.500   321.000   
5871  RPP   -346.500  -217.341   -163.909   -163.750   203.500   321.000   
5872  RPP   -217.500  -217.341   -163.750   -115.909   203.500   321.000   
5873  RPP   -217.500   247.659   -115.909   -115.750   203.500   321.000   
5874  RPP    247.500   247.659   -115.750     44.250   203.500   321.000   
5875  RPP    147.500   247.659     44.250     44.409   203.500   321.000   
c ----- Escalier plateforme -----                        
5901  RPP   -448.500  -346.500   -279.750   -177.750   198.500   210.500   $ Structure
5902  RPP   -447.500  -347.500   -279.250   -178.250   199.300   209.800   $ Air structure
5903  RPP   -442.500  -352.500   -272.750   -183.750   198.500   210.500   
5904  RPP   -427.500  -367.500   -177.750   -163.909   203.500   210.500   $ Structure +Y
5905  RPP   -424.000  -371.000   -177.750   -167.250   203.500   210.500   $ Air structure +Y
5906  RPP   -427.200  -424.300   -177.750   -164.050   203.800   210.200   
5907  RPP   -370.700  -367.800   -177.750   -164.050   203.800   210.200   
5908  RPP   -424.300  -370.700   -166.950   -164.050   203.800   210.200   
5909  RPP   -427.500  -367.500   -293.750   -279.750   203.500   210.500   $ Structure -Y
5910  RPP   -424.000  -371.000   -290.250   -279.750   203.500   210.500   $ Air structure -Y
5911  RPP   -427.200  -424.300   -293.450   -279.750   203.800   210.200   
5912  RPP   -370.700  -367.800   -293.450   -279.750   203.800   210.200   
5913  RPP   -424.300  -370.700   -293.450   -290.550   203.800   210.200   
5914  RPP   -354.500  -346.500   -185.750   -177.750     0.000   198.500   $ Potaux +X+Y
5915  RPP   -354.200  -346.800   -185.450   -178.050     0.000   198.500   $ Air Potaux +X+Y
5916  RPP   -354.500  -346.500   -279.750   -271.750     0.000   198.500   $ Potaux +X-Y
5917  RPP   -354.200  -346.800   -279.450   -272.050     0.000   198.500   $ Air Potaux +X-Y
5918  RPP   -488.500  -480.500   -185.750   -177.750     0.000   155.300   $ Potaux -X+Y
5919  RPP   -488.200  -480.800   -185.450   -178.050     0.000   155.300   $ Air Potaux -X+Y
5920  RPP   -488.500  -480.500   -279.750   -271.750     0.000   155.300   $ Potaux -X-Y
5921  RPP   -488.200  -480.800   -279.450   -272.050     0.000   155.300   $ Air Potaux -X-Y
5922  RPP   -542.500  -354.500   -185.750   -177.750    93.500   101.500   $ Barre +Y
5923  RPP   -542.500  -354.500   -185.450   -178.050    93.800   101.200   $ Air Barre +Y
5924  RPP   -542.500  -354.500   -279.750   -271.750    93.500   101.500   $ Barre -Y
5925  RPP   -542.500  -354.500   -279.450   -272.050    93.800   101.200   $ Air Barre -Y
5926  RPP   -354.500  -346.500   -271.750   -185.750    93.500   101.500   $ Barre +X
5927  RPP   -354.200  -346.800   -271.750   -185.750    93.800   101.200   $ Air Barre +X
5928  RPP   -448.500  -346.500   -279.750   -177.750   210.500   213.500   $ Caillebotie
5929  RPP   -427.500  -367.500   -177.750   -163.909   210.500   213.500   
5930  RPP   -427.500  -367.500   -293.750   -279.750   210.500   213.500   
c -----Marches -----                                
5931  RPP   -704.300  -660.000   -279.750   -177.750     0.000    19.500   $ Marche 1
5932  RPP   -704.300  -660.000   -278.750   -178.750     0.000    19.500   $ Air Marche 1
5933  RPP   -683.500  -660.000   -278.750   -178.750    16.500    19.500   $ Caillebotie Marche 1
5934  RPP   -680.800  -636.500   -279.750   -177.750    19.500    38.900   $ Marche 2
5935  RPP   -680.800  -636.500   -278.750   -178.750    19.500    38.900   $ Air Marche 2
5936  RPP   -660.000  -636.500   -278.750   -178.750    35.900    38.900   $ Caillebotie Marche 2
5937  RPP   -657.300  -613.000   -279.750   -177.750    38.900    58.300   $ Marche 3
5938  RPP   -657.300  -613.000   -278.750   -178.750    38.900    58.300   $ Air Marche 3
5939  RPP   -636.500  -613.000   -278.750   -178.750    55.300    58.300   $ Caillebotie Marche 3
5940  RPP   -633.800  -589.500   -279.750   -177.750    58.300    77.700   $ Marche 4
5941  RPP   -633.800  -589.500   -278.750   -178.750    58.300    77.700   $ Air Marche 4
5942  RPP   -613.000  -589.500   -278.750   -178.750    74.700    77.700   $ Caillebotie Marche 4
5943  RPP   -610.300  -566.000   -279.750   -177.750    77.700    97.100   $ Marche 5
5944  RPP   -610.300  -566.000   -278.750   -178.750    77.700    97.100   $ Air Marche 5
5945  RPP   -589.500  -566.000   -278.750   -178.750    94.100    97.100   $ Caillebotie Marche 5
5946  RPP   -586.800  -542.500   -279.750   -177.750    97.100   116.500   $ Marche 6
5947  RPP   -586.800  -542.500   -278.750   -178.750    97.100   116.500   $ Air Marche 6
5948  RPP   -566.000  -542.500   -278.750   -178.750   113.500   116.500   $ Caillebotie Marche 6
5949  RPP   -563.300  -519.000   -279.750   -177.750   116.500   135.900   $ Marche 7
5950  RPP   -563.300  -519.000   -278.750   -178.750   116.500   135.900   $ Air Marche 7
5951  RPP   -542.500  -519.000   -278.750   -178.750   132.900   135.900   $ Caillebotie Marche 7
5952  RPP   -539.800  -495.500   -279.750   -177.750   135.900   155.300   $ Marche 8
5953  RPP   -539.800  -495.500   -278.750   -178.750   135.900   155.300   $ Air Marche 8
5954  RPP   -519.000  -495.500   -278.750   -178.750   152.300   155.300   $ Caillebotie Marche 8
5955  RPP   -516.300  -472.000   -279.750   -177.750   155.300   174.700   $ Marche 9
5956  RPP   -516.300  -472.000   -278.750   -178.750   155.300   174.700   $ Air Marche 9
5957  RPP   -495.500  -472.000   -278.750   -178.750   171.700   174.700   $ Caillebotie Marche 9
5958  RPP   -492.800  -448.500   -279.750   -177.750   174.700   194.100   $ Marche 10
5959  RPP   -492.800  -448.500   -278.750   -178.750   174.700   194.100   $ Air Marche 10
5960  RPP   -472.000  -448.500   -278.750   -178.750   191.100   194.100   $ Caillebotie Marche 10
c -----Garde-Corps -----                            
5961  RPP   -448.500  -346.341   -279.909   -279.750   203.500   321.000   $ Garde-Corps
5962  RPP   -346.500  -346.341   -279.750   -177.750   203.500   321.000   
5963  RPP   -680.800  -657.300   -280.850   -279.750    38.900   161.900   $ Garde-Corps marches -Y
5964  RPP   -657.300  -633.800   -280.850   -279.750    58.300   181.300   
5965  RPP   -633.800  -610.300   -280.850   -279.750    77.700   200.700   
5966  RPP   -610.300  -586.800   -280.850   -279.750    97.100   220.100   
5967  RPP   -586.800  -563.300   -280.850   -279.750   116.500   239.500   
5968  RPP   -563.300  -539.800   -280.850   -279.750   135.900   258.900   
5969  RPP   -539.800  -516.300   -280.850   -279.750   155.300   278.300   
5970  RPP   -516.300  -492.800   -280.850   -279.750   174.700   297.700   
5971  RPP   -492.800  -469.300   -280.850   -279.750   194.100   317.100   
5972  RPP   -680.800  -657.300   -177.750   -176.650    38.900   161.900   $ Garde-Corps marches +Y
5973  RPP   -657.300  -633.800   -177.750   -176.650    58.300   181.300   
5974  RPP   -633.800  -610.300   -177.750   -176.650    77.700   200.700   
5975  RPP   -610.300  -586.800   -177.750   -176.650    97.100   220.100   
5976  RPP   -586.800  -563.300   -177.750   -176.650   116.500   239.500   
5977  RPP   -563.300  -539.800   -177.750   -176.650   135.900   258.900   
5978  RPP   -539.800  -516.300   -177.750   -176.650   155.300   278.300   
5979  RPP   -516.300  -492.800   -177.750   -176.650   174.700   297.700   
5980  RPP   -492.800  -469.300   -177.750   -176.650   194.100   317.100
5981  RPP   -704.300  -346.341   -293.750   -163.909     0.000   500.000   $ Englobant escalier
c ----- Plateforme Canon + 4 plots b�ton + Canon -----
6001  RPP   -947.850  -769.350    -54.000     80.000   162.500   167.500   $ Cadre
6002  RPP   -941.850  -775.350    -48.000     74.000   162.500   167.500   $ Air Cadre
6003  RPP   -947.850  -769.350    -54.000     80.000   100.000   105.000   $ Barreaux
6004  RPP   -941.850  -775.350    -48.000     74.000   100.000   105.000   $ Air Barreaux
6005  RPP   -947.850  -941.850    -54.000    -48.000    50.000   162.500   $ Pieds
6006  RPP   -947.850  -941.850     74.000     80.000    50.000   162.500   
6007  RPP   -775.350  -769.350    -54.000    -48.000    50.000   162.500   
6008  RPP   -775.350  -769.350     74.000     80.000    50.000   162.500   
6009  RPP   -957.350  -638.350    -35.250     61.250   212.500   214.300   $ Plateau
6010  RPP   -947.850  -941.850    -26.000    -20.000   167.500   212.500   $ Pieds
6011  RPP   -947.850  -941.850     46.000     52.000   167.500   212.500   
6012  RPP   -775.350  -769.350    -26.000    -20.000   167.500   212.500   
6013  RPP   -775.350  -769.350     46.000     52.000   167.500   212.500   
6014  RPP   -957.350  -827.350    -32.000     58.000   214.300   354.300   $ Canon
6015  RCC   -827.350     0.000    320.000    230.000     0   0    12.500   $ Canon Tube
6016  RPP   -970.350  -920.350    -76.500    -26.500     0.000    50.000   $ Plots b�ton
6017  RPP   -808.750  -758.750    -76.500    -26.500     0.000    50.000   
6018  RPP   -970.350  -920.350     57.200    107.200     0.000    50.000   
6019  RPP   -808.750  -758.750     57.200    107.200     0.000    50.000   
6020  RCC   -662.350    13.000      0.000      0   0   212.500     4.000   $ Tube support
6021  RPP   -769.350  -662.350      7.000     13.000   162.500   167.500   $ Barres support
6022  RPP   -769.350  -662.350     13.000     19.000   162.500   167.500   $ Barres support
c ----- Structure bleue -----
6031  RPP   -637.500  -337.500   -62.750      57.250   204.500   206.300   $ Plateau   
6032  RPP   -445.500  -337.500   -22.750      17.250   204.500   206.300   $ Air   
6033  RPP   -637.500  -337.500   -62.750     -46.750   198.000   204.500   $ Rail -Y   
6034  RPP   -637.500  -636.500   -61.700     -47.800   198.000   203.450   $ Air   
6035  RPP   -622.500  -519.500   -61.700     -47.800   198.000   203.450      
6036  RPP   -505.500  -352.500   -61.700     -47.800   198.000   203.450      
6037  RPP   -338.500  -337.500   -61.700     -47.800   198.000   203.450      
6038  RPP   -637.500  -337.500    41.250      57.250   198.000   204.500   $ Rail -Y   
6039  RPP   -637.500  -636.500    42.300      56.200   198.000   203.450   $ Air   
6040  RPP   -622.500  -519.500    42.300      56.200   198.000   203.450      
6041  RPP   -505.500  -352.500    42.300      56.200   198.000   203.450      
6042  RPP   -338.500  -337.500    42.300      56.200   198.000   203.450      
6043  RCC   -629.500   -54.750   193.000       0   0     5.000     2.100   $ Tiges   
6044  RCC   -512.500   -54.750   193.000       0   0     5.000     2.100      
6045  RCC   -345.500   -54.750   193.000       0   0     5.000     2.100      
6046  RCC   -629.500    49.250   193.000       0   0     5.000     2.100      
6047  RCC   -512.500    49.250   193.000       0   0     5.000     2.100      
6048  RCC   -345.500    49.250   193.000       0   0     5.000     2.100      
6049  RPP   -627.714   -27.214    -13.750     13.750   173.500   201.600   $ Gros rail   
6050  RPP   -627.714   -27.214    -11.250     11.250   200.100   201.600   $ Air sup   
6051  RPP   -627.714   -27.214    -13.750     -0.600   174.700   198.900   $ Air -Y   
6052  RPP   -627.714   -27.214      0.600     13.750   174.700   198.900   $ Air +Y   
6053  RCC   -602.932    -0.600    186.800      0   1.200   0       7.500   $ Trous
6054  RCC   -542.932    -0.600    186.800      0   1.200   0       7.500   
6055  RCC   -482.932    -0.600    186.800      0   1.200   0       7.500   
6056  RCC   -422.932    -0.600    186.800      0   1.200   0       7.500   
6057  RCC   -362.932    -0.600    186.800      0   1.200   0       7.500   
6058  RCC   -302.932    -0.600    186.800      0   1.200   0       7.500   
6059  RCC   -242.932    -0.600    186.800      0   1.200   0       7.500   
6060  RCC   -182.932    -0.600    186.800      0   1.200   0       7.500   
6061  RCC   -122.932    -0.600    186.800      0   1.200   0       7.500   
6062  RPP   -633.500  -625.500    -58.750    -50.750     0.000   193.000   $ Pieds   
6063  RPP   -516.500  -508.500    -58.750    -50.750    56.500   193.000      
6064  RPP   -349.500  -341.500    -58.750    -50.750    56.500   193.000      
6065  RPP   -633.500  -625.500     46.250     54.250     0.000   193.000      
6066  RPP   -516.500  -508.500     46.250     54.250    56.500   193.000      
6067  RPP   -349.500  -341.500     46.250     54.250    56.500   193.000      
6068  RPP   -625.500  -349.500    -58.750    -50.750    66.500    74.500   $ Barres horizontales   
6069  RPP   -625.500  -349.500    -58.750    -50.750   179.500   187.500      
6070  RPP   -625.500  -349.500     46.250     54.250    66.500    74.500      
6071  RPP   -625.500  -349.500     46.250     54.250   179.500   187.500      
6072  RPP   -633.500  -625.500    -50.750     46.250    56.500    64.500      
6073  RPP   -633.500  -625.500    -50.750     46.250   154.500   162.500      
6074  RPP   -516.500  -508.500    -50.750     46.250    56.500    64.500      
6075  RPP   -516.500  -508.500    -50.750     46.250   154.500   162.500      
6076  RPP   -349.500  -341.500    -50.750     46.250    56.500    64.500      
6077  RPP   -349.500  -341.500    -50.750     46.250   154.500   162.500      
6078  RPP   -575.000  -567.000    -58.750    -50.750    74.500   179.500   $ Barres diag=verticales   
6079  RPP   -575.000  -567.000     46.250     54.250    74.500   179.500      
6080  RPP   -633.500  -625.500     -6.250      1.750    64.500   154.500      
6081  RPP   -516.500  -508.500     -6.250      1.750    64.500   154.500      
6082  RPP   -349.500  -341.500     -6.250      1.750    64.500   154.500      
6083  RPP   -508.500  -349.500    -58.750    -50.750   123.000   131.000   $ Barres diag=horizontales   
6084  RPP   -508.500  -349.500     46.250     54.250   123.000   131.000      
6085  RPP   -520.500  -504.500    -58.750     54.250    50.000    56.500   $ Poutres en U   
6086  RPP   -353.500  -337.500    -58.750     54.250    50.000    56.500      
6087  RPP   -519.450  -505.550    -58.750     54.250    50.000    55.450   $ Air   
6088  RPP   -352.450  -338.550    -58.750     54.250    50.000    55.450      
c ----- Portiques gris -----                           
6090  RPP   -565.500  -559.500    -30.000    -27.000    50.000   150.000   $ Pieds -Y   
6091  RPP   -565.500  -559.500     27.000     30.000    50.000   150.000   $ Pieds +Y   
6092  RPP   -565.500  -559.500    -27.000     27.000   147.000   150.000   $ Barre   
6093  RCC   -562.500   -25.000    150.000      0   0    44.000     2.100   $ Tiges   
6094  RCC   -562.500    25.000    150.000      0   0    44.000     2.100      
6095  RPP   -570.500  -554.500    -30.000     30.000   167.000   173.500   $ Barre bleu   
6096  RPP   -569.450  -555.550    -20.000     20.000   167.000   172.450   $ Aire Barre bleu   
6097  RPP   -368.500  -362.500    -30.000    -27.000    50.000   150.000   $ Pieds -Y   
6098  RPP   -368.500  -362.500     27.000     30.000    50.000   150.000   $ Pieds +Y   
6099  RPP   -368.500  -362.500    -27.000     27.000   147.000   150.000   $ Barre   
6100  RCC   -365.500   -25.000    150.000      0   0    44.000     2.100   $ Tiges   
6101  RCC   -365.500    25.000    150.000      0   0    44.000     2.100      
6102  RPP   -373.500  -357.500    -30.000     30.000   167.000   173.500   $ Barre bleu   
6103  RPP   -372.450  -358.550    -20.000     20.000   167.000   172.450   $ Aire Barre bleu   
6104  RPP   -293.500  -287.500    -30.000    -27.000    50.000   150.000   $ Pieds -Y   
6105  RPP   -293.500  -287.500     27.000     30.000    50.000   150.000   $ Pieds +Y   
6106  RPP   -293.500  -287.500    -27.000     27.000   147.000   150.000   $ Barre   
6107  RCC   -290.500   -25.000    150.000      0   0    44.000     2.100   $ Tiges   
6108  RCC   -290.500    25.000    150.000      0   0    44.000     2.100      
6109  RPP   -298.500  -282.500    -30.000     30.000   167.000   173.500   $ Barre bleu   
6110  RPP   -297.450  -283.550    -20.000     20.000   167.000   172.450   $ Aire Barre bleu   
6111  RPP    -95.500   -89.500    -30.000    -27.000    50.000   150.000   $ Pieds -Y   
6112  RPP    -95.500   -89.500     27.000     30.000    50.000   150.000   $ Pieds +Y   
6113  RPP    -95.500   -89.500    -27.000     27.000   147.000   150.000   $ Barre   
6114  RCC    -92.500   -25.000    150.000      0   0    44.000     2.100   $ Tiges   
6115  RCC    -92.500    25.000    150.000      0   0    44.000     2.100      
6116  RPP   -100.500   -84.500    -30.000     30.000   167.000   173.500   $ Barre bleu   
6117  RPP    -99.450   -85.550    -20.000     20.000   167.000   172.450   $ Aire Barre bleu   
6118  RPP   -604.500  -504.500    -52.250     47.750     0.000    50.000   $ Blocs B�ton   
6119  RPP   -376.500  -276.500    -52.250     47.750     0.000    50.000      
6120  RPP   -143.000   -43.000    -52.250     47.750     0.000    50.000      
c ----- Support Cam�ra -----                           
6121  RPP    105.986   110.986     -9.500      9.500     0.000   170.200   $ Poteau   
6122  RCC    108.486    -7.000    170.200      0   0    19.500     1.600   $ Tiges   
6123  RCC    108.486     7.000    170.200      0   0    19.500     1.600      
6124  RCC    108.486    -7.000    188.700      0   0     1.000     5.000   $ Rondelles   
6125  RCC    108.486     7.000    188.700      0   0     1.000     5.000      
6126  RPP     96.000   126.000    -13.750     13.750   196.100   293.600   $ Support cam�ra   
6127  RPP     96.000   126.000    -11.250     11.250   205.100   290.100   $ air support cam�ra   
6128  RPP     98.500   123.500    -13.750     13.750   205.100   290.100      
6129  RPP     98.500   123.500    -11.250     11.250   202.600   292.600      
6130  RCC     97.250   -11.550    293.600      0   0     5.500     0.852   $ Tiges   
6131  RCC     97.250    11.550    293.600      0   0     5.500     0.852      
6132  RCC    124.750    -0.250    293.600      0   0     5.500     0.852      
6133  RPP     96.000   126.000    -13.750     13.750   299.100   300.600   $ Plaque cam�ra 1   
6134  RPP    102.000   120.000     -9.750      9.750   299.100   300.600   $ Air plaque cam�ra 1   
6135  RPP     99.000   102.000     -9.750      9.750   300.600   303.600   $ Plaque support sup   
6136  RPP    120.000   123.000     -9.750      9.750   300.600   303.600      
6137  RPP    102.000   120.000     -9.750      9.750   300.600   303.600   $ Air Plaque support sup   
6138  RPP     99.700   122.300     -7.500      7.500   303.600   304.600   $ Plaque cam�ra 2   
6139  RCC    106.210    -4.900    304.600      0   0     4.500     0.500   $ Tiges   
6140  RCC    106.210     4.900    304.600      0   0     4.500     0.500      
6141  RCC    117.020    -0.060    304.600      0   0     4.500     0.500      
6142  RPP    103.500   118.500     -7.500      7.500   309.100   311.100   $ Plaque cam�ra 3   
6143  RPP     96.000   126.000    -13.750     13.750   292.600   293.600   $ Plaque cam�ra 0   
C ************************************ C
C ***** PLATEFORME ET LIGNE T400 ***** C
C ************************************ C
c ----- T400 - Structure support -----                        
6150  RPP  -1024.700 -1016.700    273.750   417.750     42.000    50.000   $ Structure -X haut
6151  RPP   -842.700  -834.700    273.750   417.750     42.000    50.000   
6152  RPP   -959.700  -951.700    281.750   409.750     42.000    50.000   
6153  RPP   -899.700  -891.700    281.750   409.750     42.000    50.000   
6154  RPP  -1016.700  -842.700    273.750   281.750     42.000    50.000   
6155  RPP  -1016.700  -842.700    409.750   417.750     42.000    50.000   
6156  RPP  -1024.700 -1016.700    273.750   417.750     11.000    19.000   $ Structure -X bas
6157  RPP   -842.700  -834.700    273.750   417.750     11.000    19.000   
6158  RPP   -932.700  -924.700    281.750   409.750     11.000    19.000   
6159  RPP  -1016.700  -842.700    273.750   281.750     11.000    19.000   
6160  RPP  -1016.700  -842.700    409.750   417.750     11.000    19.000   
6161  RPP   -959.700  -951.700    273.750   281.750     19.000    42.000   $ Renforts
6162  RPP   -899.700  -891.700    273.750   281.750     19.000    42.000   
6163  RPP   -959.700  -951.700    409.750   417.750     19.000    42.000   
6164  RPP   -899.700  -891.700    409.750   417.750     19.000    42.000   
6165  RPP  -1024.700 -1016.700    273.750   281.750      0.000    42.000   $ Pieds
6166  RPP  -1024.700 -1016.700    409.750   417.750      0.000    42.000   
6167  RPP   -842.700  -834.700    273.750   281.750      0.000    42.000   
6168  RPP   -842.700  -834.700    409.750   417.750      0.000    42.000   
6169  RPP   -834.700  -638.700    305.750   313.750     42.000    50.000   $ Structure milieu
6170  RPP   -834.700  -638.700    377.750   385.750     42.000    50.000   
6171  RPP   -834.700  -638.700    305.750   313.750     11.000    19.000   
6172  RPP   -834.700  -638.700    377.750   385.750     11.000    19.000   
6173  RPP   -769.700  -761.700    313.750   377.750     42.000    50.000   $ Barres
6174  RPP   -695.700  -687.700    313.750   377.750     42.000    50.000   
6175  RPP   -785.700  -777.700    313.750   377.750     11.000    19.000   
6176  RPP   -695.700  -687.700    313.750   377.750     11.000    19.000   
6177  RPP   -785.700  -777.700    305.750   313.750      0.000    42.000   $ Pieds
6178  RPP   -785.700  -777.700    377.750   385.750      0.000    42.000   
6179  RPP   -695.700  -687.700    305.750   313.750      0.000    42.000   
6180  RPP   -695.700  -687.700    377.750   385.750      0.000    42.000   
6181  RPP   -761.700  -757.700    343.750   347.750     42.000   183.000   $ Structure milieu sup
6182  RPP   -757.700  -692.700    343.750   347.750    179.000   183.000   
6183  RPP   -692.700  -688.700    343.750   347.750     54.000   203.200   
6184  RPP   -692.700  -688.700    309.750   381.750     50.000    54.000   
6185  RPP   -692.700  -688.700    313.750   343.750     82.000    86.000   
6186  RPP   -692.700  -688.700    347.750   377.750     82.000    86.000   
6187  RPP   -692.700  -688.700    309.750   313.750     54.000    86.000   
6188  RPP   -692.700  -688.700    377.750   381.750     54.000    86.000   
6189  RPP   -638.700  -346.700    289.250   297.250     11.000    19.000   $ Structure +X
6190  RPP   -638.700  -346.700    394.250   402.250     11.000    19.000   
6191  RPP   -638.700  -630.700    297.250   394.250     11.000    19.000   
6192  RPP   -529.700  -521.700    297.250   394.250     11.000    19.000   
6193  RPP   -354.700  -346.700    297.250   394.250     11.000    19.000   
6194  RPP   -638.700  -346.700    289.250   297.250     89.000    97.000   
6195  RPP   -638.700  -346.700    394.250   402.250     89.000    97.000   
6196  RPP   -638.700  -630.700    297.250   394.250     69.000    77.000   
6197  RPP   -529.700  -521.700    297.250   394.250     69.000    77.000   
6198  RPP   -354.700  -346.700    297.250   394.250     69.000    77.000   
6199  RPP   -638.700  -630.700    289.250   297.250      0.000   104.000   $ Pieds
6200  RPP   -529.700  -521.700    289.250   297.250      0.000   104.000   
6201  RPP   -354.700  -346.700    289.250   297.250      0.000   104.000   
6202  RPP   -638.700  -630.700    394.250   402.250      0.000   104.000   
6203  RPP   -529.700  -521.700    394.250   402.250      0.000   104.000   
6204  RPP   -354.700  -346.700    394.250   402.250      0.000   104.000   
6205  RPP   -630.700  -354.700    289.250   297.250     69.000    77.000   $ Barre diag
6206  RPP   -630.700  -354.700    394.250   402.250     69.000    77.000   
6207  RCC   -634.700   293.250    104.000     0   0     13.000     2.100   $ Tiges
6208  RCC   -525.700   293.250    104.000     0   0     13.000     2.100   
6209  RCC   -350.700   293.250    104.000     0   0     13.000     2.100   
6210  RCC   -634.700   398.250    104.000     0   0     13.000     2.100   
6211  RCC   -525.700   398.250    104.000     0   0     13.000     2.100   
6212  RCC   -350.700   398.250    104.000     0   0     13.000     2.100   
6213  RPP   -643.700  -244.700    289.250   402.250    123.500   125.300   $ Plateau
6214  RPP   -643.700  -244.700    289.250   305.250    117.000   123.500   $ Poutres U
6215  RPP   -643.700  -244.700    386.250   402.250    117.000   123.500   
6216  RPP   -643.700  -641.700    290.300   304.200    117.000   122.450   $ Air Poutres (+/- 7 cm en X autour des tiges)
6217  RPP   -627.700  -532.700    290.300   304.200    117.000   122.450   
6218  RPP   -518.700  -357.700    290.300   304.200    117.000   122.450   
6219  RPP   -343.700  -258.700    290.300   304.200    117.000   122.450   
6220  RPP   -643.700  -641.700    387.300   401.200    117.000   122.450   
6221  RPP   -627.700  -532.700    387.300   401.200    117.000   122.450   
6222  RPP   -518.700  -357.700    387.300   401.200    117.000   122.450   
6223  RPP   -343.700  -258.700    387.300   401.200    117.000   122.450   
6224  RPP   -614.700  -604.700    313.250   378.250    125.300   126.500   $ Traverses
6225  RPP   -564.700  -554.700    313.250   378.250    125.300   126.500   
6226  RPP   -514.700  -504.700    313.250   378.250    125.300   126.500   
6227  RPP   -464.700  -454.700    313.250   378.250    125.300   126.500   
6228  RPP   -414.700  -404.700    313.250   378.250    125.300   126.500   
6229  RPP   -364.700  -354.700    313.250   378.250    125.300   126.500   
6230  RPP   -314.700  -304.700    313.250   378.250    125.300   126.500   
6231  RPP   -264.700  -254.700    313.250   378.250    125.300   126.500   
6232  RPP   -643.700  -254.700    320.750   330.750    126.500   131.500   $ Rails
6233  RPP   -643.700  -254.700    321.600   329.900    126.500   130.950   
6234  RPP   -643.700  -254.700    360.750   370.750    126.500   131.500   
6235  RPP   -643.700  -254.700    361.600   369.900    126.500   130.950   
6236  RPP   -628.700  -523.700    292.025   295.475    125.300   126.850   $ Rails guides
6237  RPP   -476.700  -371.700    292.025   295.475    125.300   126.850   
6238  RPP   -628.700  -523.700    396.025   399.475    125.300   126.850   
6239  RPP   -476.700  -371.700    396.025   399.475    125.300   126.850   
6240  RPP  -1074.300  -807.300    260.250   431.250      0.000   100.000   $ Casson en bois
6241  RPP  -1072.300  -809.300    262.250   429.250      0.000    98.000   
c ----- plateforme -----                        
6242  RPP   -651.700  -346.700    402.250   498.750    115.300   122.300   $ Plateforme (idem H Van Gogh)
6243  RPP   -648.200  -350.200    405.750   495.250    115.300   122.300   $ Air plateforme
6244  RPP   -651.700  -346.700    402.250   498.750    122.300   125.300   $ Caillebotis
6245  RPP   -619.700  -613.700    405.750   495.250    116.300   122.300   $ Pieds 1
6246  RPP   -619.700  -613.700    405.750   411.750      0.000   116.300   
6247  RPP   -619.700  -613.700    489.250   495.250      0.000   116.300   
6248  RPP   -619.700  -613.700    411.750   489.250     66.300    72.300   
6249  RPP   -386.700  -380.700    405.750   495.250    116.300   122.300   $ Pieds 2
6250  RPP   -386.700  -380.700    405.750   411.750      0.000   116.300   
6251  RPP   -386.700  -380.700    489.250   495.250      0.000   116.300   
6252  RPP   -386.700  -380.700    411.750   489.250     66.300    72.300   
c ----- Marches -----                        
6253  RPP   -252.700  -208.400    402.250   498.750      0.000    20.890   $ Marche 1
6254  RPP   -252.700  -208.400    405.750   495.250      0.000    20.890   $ Air Marche 1
6255  RPP   -252.700  -226.200    405.750   495.250     17.890    20.890   $ Caillebotie Marche 1
6256  RPP   -276.200  -231.900    402.250   498.750     20.890    41.780   $ Marche 2
6257  RPP   -276.200  -231.900    405.750   495.250     20.890    41.780   $ Air Marche 2
6258  RPP   -276.200  -249.700    405.750   495.250     38.780    41.780   $ Caillebotie Marche 2
6259  RPP   -299.700  -255.400    402.250   498.750     41.780    62.670   $ Marche 3
6260  RPP   -299.700  -255.400    405.750   495.250     41.780    62.670   $ Air Marche 3
6261  RPP   -299.700  -273.200    405.750   495.250     59.670    62.670   $ Caillebotie Marche 3
6262  RPP   -323.200  -278.900    402.250   498.750     62.670    83.560   $ Marche 4
6263  RPP   -323.200  -278.900    405.750   495.250     62.670    83.560   $ Air Marche 4
6264  RPP   -323.200  -296.700    405.750   495.250     80.560    83.560   $ Caillebotie Marche 4
6265  RPP   -346.700  -302.400    402.250   498.750     83.560   104.450   $ Marche 5
6266  RPP   -346.700  -302.400    405.750   495.250     83.560   104.450   $ Air Marche 5
6267  RPP   -346.700  -320.200    405.750   495.250    101.450   104.450   $ Caillebotie Marche 5
6268  RPP   -651.700  -346.700    498.750   498.909    115.300   232.800   $ Garde-Corps
6269  RPP   -651.859  -651.700    402.250   498.750    115.300   232.800
c ----- Ligne T400 -----
6301  RCC   -623.900   345.750    230.000     1.400      0   0     4.800       $ Aluminium Porte-cible   
6302  RCC   -623.900   345.750    230.000     1.400      0   0     1.800       $ Vide dans le porte-cible   
6303  RCC   -622.500   345.750    230.000     1.500      0   0     2.500       $ Aluminium Porte-cible   
6304  RCC   -622.500   345.750    230.000     1.500      0   0     1.800       $ Vide dans le porte-cible   
6305  RCC   -621.000   345.750    230.000     0.100      0   0     2.500       $ Backing en Cuivre   
6306  RCC   -622.500   345.750    230.000     1.700      0   0     2.750       $ Eau de refroidissement   
6307  RCC   -622.500   345.750    230.000     1.500      0   0     4.800       $ Aluminium Porte-cible   
6308  RCC   -621.000   345.750    230.000     0.300      0   0     3.100       $ Aluminium Porte-cible   
6309  TRC   -640.800   345.750    230.000    16.900      0   0     2.975 1.800 $ Vide Int Cone      SuperMC X = -632.350, MCNP X = -640.800
6310  TRC   -640.800   345.750    230.000    16.900      0   0     3.675 2.500 $ Aluminium Ext Cone SuperMC X = -632.350, MCNP X = -640.800
6311  RCC   -641.700   345.750    230.000     0.900      0   0     8.000       $ Aluminium Bride
6312  RCC   -641.700   345.750    230.000     0.900      0   0     2.975       $ Vide Bride
6313  RCC   -644.900   345.750    230.000     3.200      0   0     4.000   $ Air Vanne VAT
6314  RCC   -644.900   345.750    230.000     3.200      0   0     5.900   $ Corps Vanne VAT
6315  RPP   -644.900  -641.700    339.850   351.650    218.400   230.000   
6316  RPP   -645.100  -641.500    342.075   349.425    212.650   218.400   
6317  RCC   -643.300   345.750    193.700     0   0     18.950     2.150   $ Manche Vanne VAT
6318  RCC   -640.800   345.750    230.000     4.000      0   0     5.000   $ "Cible" photo IMG_0219.jpg
6319  RCC   -638.800   345.750    214.000     0   0     16.000     1.000   $ �quip. Inf
6320  RCC   -638.800   345.750    230.000     0   0      8.000     0.500   $ �quip. Sup
6321  RCC   -638.800   345.750    238.000     0   0      6.000     1.500   
6322  RCC   -638.800   345.750    244.000     0   0      4.000     1.600
6323  RCC   -645.800   345.750    230.000     0.900      0   0     8.000   $ Bride                 
6324  RCC   -645.800   345.750    230.000     0.900      0   0     2.975   $ Air Bride             
6325  RCC   -649.500   345.750    230.000     3.700      0   0     3.750   $ Goulot Module
6326  RCC   -649.845   345.750    230.000     4.045      0   0     3.350   $ Vide Goulot Module diag
6327  RCC   -709.9069  345.750    230.000    60.4069     0   0    10.5831  $ Module Diag        
6328  RCC   -709.5619  345.750    230.000    59.7169     0   0    10.1899  $ Vide Module Diag
6329 1 CX      0.2050                                                      $ Passage diode C  
6330 1 CX      1.9000                                                      $ Tube Diode C     
6331 1 CX      1.4000                                                      $ Vide Tube Diode C
6332 1 CX      0.8350                                                      $ Diode C          
6333 1 CX      0.4000                                                      $ Vide Diode C     
6334 1 CX      2.5000                                                      $ Fixation Diode C
6335   PX   -709.5619
6336   PX   -709.9069
6338 1 PX      0.0000  
6339 1 PX     -1.2300
6349 2 CX      0.2025                                                      $ Passage diode A  
6350 2 CX      1.9000                                                      $ Tube Diode A     
6351 2 CX      1.4000                                                      $ Vide Tube Diode A
6352 2 CX      0.8350                                                      $ Diode A          
6353 2 CX      0.4000                                                      $ Vide Diode A     
6354 2 CX      2.5000                                                      $ Fixation Diode A 
6358 2 PX      0.0000                     
6359 2 PX     -1.2300                    
6369 3 CX      0.2050                                                      $ Passage diode B  
6370 3 CX      1.9000                                                      $ Tube Diode B     
6371 3 CX      1.4000                                                      $ Vide Tube Diode B
6372 3 CX      0.8350                                                      $ Diode B          
6373 3 CX      0.4000                                                      $ Vide Diode B     
6374 3 CX      2.5000                                                      $ Fixation Diode B 
6378 3 PX      0.0000                     
6379 3 PX     -1.2300                    
6381  RCC   -717.9069  345.750    230.000     8.000      0   0     3.750   $ Sortie Arr. Diag     
6382  RCC   -718.3069  345.750    230.000     8.745      0   0     3.350   $ Vide Sortie Arr. Diag
6383  RCC   -718.3069  345.750    230.000     0.400      0   0     4.000   $ Bride
6384  RCC   -718.907   345.750    230.000     0.6001     0   0     3.900   $ Piege � �lectron (6) Bride av
6385  RCC   -723.707   345.750    230.000     4.800      0   0     3.250   $ Piege � �lectron (6) Tube      
6386  RCC   -724.307   345.750    230.000     0.600      0   0     3.900   $ Piege � �lectron (6) Bride ar  
6387  RCC   -724.307   345.750    230.000     3.000      0   0     2.800   $ air Piege � �lectron (6)       
6388  RCC   -721.307   345.750    230.000     3.0001     0   0     2.900
6389  RCC   -733.307   345.750    230.000     0.600      0   0     3.900   $ Diaphragme (5) Bride ar
6390  RCC   -732.707   345.750    230.000     7.800      0   0     3.600   $ Diaphragme (5) Tube    
6391  RCC   -724.907   345.750    230.000     0.600      0   0     3.900   $ Diaphragme (5) Bride av
6392  RCC   -733.307   345.750    230.000     9.000      0   0     2.900   $ Diaphragme (5) vIde    
6393  RCC   -739.307   345.750    225.000     6.000      0   0    10.000   $ Interface vide / cible (4)
6394  RCC   -739.307   345.750    230.000     6.000      0   0     2.900   $ Vide Interface              
6395  RCC   -751.307   345.750    230.000    12.000      0   0     3.250   $ Tube (3) / (4)            
6396  RCC   -751.307   345.750    230.000    12.000      0   0     2.900   $ Vide Tube (3) / (4)       
6397  RCC   -754.307   345.750    227.000     3.000      0   0     7.500   $ Vanne manuelle (3)          
6398  RCC   -759.807   345.750    224.000     5.500      0   0    14.000                               
6399  RCC   -760.807   345.750    230.000     9.500      0   0     2.900   $ Vide Vanne manuelle (3)
6400  RCC   -783.807   345.750    230.000    24.000      0   0     8.000   $ Pi�ce fonderie (2)
6401  RCC   -783.807   345.750    230.000    23.000      0   0     7.000   $ Vide Pi�ce fonderie (2)
6402  RCC   -771.807   345.750    215.000     0   0     15.000     8.000   $ Liaison Pompe / (2)
6403  RCC   -771.807   345.750    215.000     0   0     15.000     7.000   $ Vide Liaison Pompe / (2)
6404  RCC   -771.807   345.750    210.000     0   0      5.000    11.000   $ Pompe � vide (13) corps 1
6405  RCC   -771.807   345.750    204.000     0   0      6.000     8.000   $ Pompe � vide (13) corps 2  
6406  RCC   -771.807   345.750    194.000     0   0     10.000     8.500   $ Pompe � vide (13) corps 3  
6407  RCC   -771.807   345.750    189.500     0   0      4.500     6.000   $ Pompe � vide (13) corps 4  
6408  RCC   -771.807   345.750    210.000     0   0      5.000     6.000   $ Vide Pompe � vide (13)     
6409  RCC   -771.807   345.750    204.000     0   0      6.000     7.000                                
6410  RCC   -771.807   345.750    195.000     0   0      9.000     7.500
6411  RPP  -1031.000  -807.300    295.750   395.750    100.000   101.000   $ Plaque canon T400
6412  RCC   -984.200   345.750    101.000     0   0     89.000    22.500   $ Support canon T400   
6413  RPP  -1034.200  -924.200    300.750   390.750    190.000   270.000   $ Casson canon T400
6414  RCC   -924.200   345.750    230.000   140.393      0   0    15.000   $ Canon T400
6415  RCC   -924.200   345.750    230.000   140.393      0   0     8.000   $ Tube Canon T400     
6416  RCC   -924.200   345.750    230.000   140.393      0   0     7.000   $ Vide Tube Canon T400
c ----- Cible TiD -----
6417  RCC -621.00023   345.750    230.000     2.3e-4     0   0     1.500   $ Cible TiD
c ----- support module diag, cablages -----
6418  RCC   -690.200   340.000    225.000     0     2.600    0    50.400   $ Cablage
6419  RCC   -690.200   340.000    225.000     0     2.600    0    53.000   
6420  PZ     225.000                  
6421  RPP   -698.450  -682.950    338.250    353.250   203.200   206.200   $ Plaque support Module diodes
6422  RPP   -706.700  -649.500    335.450    356.050   206.200   225.000   $ Support Module diodes
6423  RPP   -706.700  -649.500    336.450    355.050   207.200   225.000   $ air Support Module diodes
C ************************** C
C ***** BLOG - RETRAIT ***** C
C ************************** C
6450  56 RPP  387.9 510.4 7 137 165 295 $ PEHD
6451  56 RPP  392.84 510.4 11.79 132.21 169.91 290.09 $ Graphite
6452  56 RPP  378.4 567.9 13.25 26.75 138 165 $ Chassis
6453  56 RPP  378.4 567.9 117.25 130.75 138 165 
6454  56 RPP  378.4 567.9 13.25 19.67 139.02 163.98 $ Air
6455  56 RPP  378.4 567.9 20.33 26.75 139.02 163.98 
6456  56 RPP  378.4 567.9 117.25 123.67 139.02 163.98 
6457  56 RPP  378.4 567.9 124.33 130.75 139.02 163.98 
6458  56 RPP  387.9 396.4 7 137 143 165 $ UPE 220
6459  56 RPP  388.55 396.4 7 137 144.2 163.8 
6460  56 RPP  504.4 512.9 7 137 143 165 
6461  56 RPP  504.4 512.25 7 137 144.2 163.8 
6462  56 RPP  387.9 512.9 67.75 76.25 143 165 
6463  56 RPP  387.9 512.9 68.95 76.25 144.2 163.8 
6464  56 RPP  378.4 378.9 7 13.25 131.8 165 $ Patins
6465  56 RPP  387.4 387.9 7 13.25 131.8 165 
6466  56 RPP  374.15 392.15 5.125 15.125 131.3 131.8 
6467  56 RPP  445.65 446.15 7 13.25 131.8 165 
6468  56 RPP  454.65 455.15 7 13.25 131.8 165 
6469  56 RPP  441.4 459.4 5.125 15.125 131.3 131.8 
6470  56 RPP  503.9 504.4 7 13.25 131.8 165 
6471  56 RPP  512.9 513.4 7 13.25 131.8 165 
6472  56 RPP  499.65 517.65 5.125 15.125 131.3 131.8 
6473  56 RPP  378.4 378.9 130.75 137 131.8 165 
6474  56 RPP  387.4 387.9 130.75 137 131.8 165 
6475  56 RPP  374.15 392.15 128.875 138.875 131.3 131.8 
6476  56 RPP  445.65 446.15 130.75 137 131.8 165 
6477  56 RPP  454.65 455.15 130.75 137 131.8 165 
6478  56 RPP  441.4 459.4 128.875 138.875 131.3 131.8 
6479  56 RPP  503.9 504.4 130.75 137 131.8 165 
6480  56 RPP  512.9 513.4 130.75 137 131.8 165 
6481  56 RPP  499.65 517.65 128.875 138.875 131.3 131.8 
6482  56 RCC  403 19.45 132.5 0 1.1 0 5 $ Roues :-)
6483  56 RCC  555 19.45 132.5 0 1.1 0 5 
6484  56 RCC  403 123.45 132.5 0 1.1 0 5 
6485  56 RCC  555 123.45 132.5 0 1.1 0 5 
6486  56 RCC  387.9 72 230 2.5 0 0 7.8 $ Trou face arri�re Blog
6487  56 RCC  390.4 72 230 15 0 0 5.8 
c ----- Englobants BLOG RETRAIT -----
6488  56 RPP  387.9 512.9 26.75 117.25 143 165 $ Englobant sous BLOG RETRAIT
6489  56 RPP  374.15 567.9 5.125 26.75 127.5 165 $ Englobant rail -Y BLOG RETRAIT
6490  56 RPP  374.15 567.9 117.25 138.875 127.5 165 $ Englobant rail +Y BLOG RETRAIT
C *********************** C
C ***** CANEL - SUD ***** C
C *********************** C
c ----- Support Canel -----
6500  57 RPP  -0.5 110.5 -55.25 -50.25 -85.5 2.5 $ Cadre vertical -Y
6501  57 RPP  4.5 105.5 -55.25 -50.25 -80.5 -2.5 
6502  57 RPP  -0.5 110.5 50.25 55.25 -85.5 2.5 $ Cadre vertical +Y
6503  57 RPP  4.5 105.5 50.25 55.25 -80.5 -2.5 
6504  57 RPP  47 52 -50.25 50.25 -85.5 -51 $ Gd cadre
6505  57 RPP  47 52 -50.25 50.25 -80.5 -56 
6506  57 RPP  82 87 -50.25 50.25 -85.5 -51 
6507  57 RPP  82 87 -50.25 50.25 -80.5 -56 
6508  57 RPP  47 105.5 -55.25 -50.25 -56 -51 
6509  57 RPP  47 105.5 50.25 55.25 -56 -51 
6510  57 RPP  47 52 -55.25 -50.25 -80.5 -56 
6511  57 RPP  82 87 -55.25 -50.25 -80.5 -56 
6512  57 RPP  47 52 50.25 55.25 -80.5 -56 
6513  57 RPP  82 87 50.25 55.25 -80.5 -56 
6514  57 RPP  22.5 47 -44.5 44.5 -56 -51 $ Petit cadre
6515  57 RPP  27.5 47 -39.5 39.5 -56 -51 
6516  57 RPP  22.5 47 -44.5 44.5 -85.5 -80.5 
6517  57 RPP  27.5 47 -39.5 39.5 -85.5 -80.5 
6518  57 RPP  22.5 27.5 -44.5 -39.5 -80.5 -56 
6519  57 RPP  22.5 27.5 39.5 44.5 -80.5 -56 
6520  57 RPP  -13.5 110.5 -55.25 55.25 -88.5 -85.5 $ Plateau inf
6521  57 RPP  27.5 95.5 -39.5 39.5 -88.5 -85.5 
6522  57 RPP  19 110.5 -20 20 -51 -50 $ Plateau sup
6523  57 RCC  -2.25 -56.75 -94.75 0 8 0 6.25 $ Roues
6524  57 RCC  -2.25 48.75 -94.75 0 8 0 6.25 
6525  57 RCC  99.25 -56.75 -94.75 0 8 0 6.25 
6526  57 RCC  99.25 48.75 -94.75 0 8 0 6.25 
c ----- Canel -----
6531  57 P    0 1 -1 -70.7107 $ Bloc CH2
6532  57 P    0 1 1 -70.7107 
6533  57 P    0 1 -1 70.7107 
6534  57 P    0 1 1 70.7107 
6535  57 PX   0 
6536  57 PX   5 
6537  57 PY   -50 
6538  57 PY   50 
6539  57 PZ   -50 
6540  57 PZ   50 
6541  57 PX   15 
6542  57 PX   17 
6543  57 PX   110.5 
6544  57 RCC  5 0 0 10 0 0 35 $ Air 10 cm polyethylene
6545  57 RCC  17 0 0 93.5 0 0 35 $ Air 93.5 cm polyethylene
6546  57 RCC  57.3 0 0 3.5 0 0 35 $ Poly layer (e=3.5 cm)
6547  57 SX   17 32 $ Grande coquille Fer
6548  57 SX   17 17.5 $ Petite coquille Fer
6549  57 SX   17 17.35 $ Grande coquille Uranium
6550  57 SX   17 5.5 $ Paroi acier coquille Uranium
6551  57 SX   17 5.3 $ Petite coquille Uranium
6552  57 PX   17.2 
6553  57 RCC  5 0 0 12 0 0 17.5 $ Manchon d'acier
6554  57 RCC  5 0 0 12 0 0 17.35 $ Manchon Uranium
6555  57 RCC  5 0 0 12 0 0 5.5 $ Manchon d'acier
6556  57 RCC  5 0 0 12 0 0 5.3 $ Air autour porte-cible
6557  57 RCC  0 0 0 5 0 0 5.5 $ Cyl. Air dans polyethylene e=5 cm
6558  57 RCC  5 0 0 8.6 0 0 3.35 $ Aluminium Porte-cible
6559  57 RCC  5 0 0 8.6 0 0 2.65 $ Vide dans le porte-cible
6560  57 RCC  13.6 0 0 1.4 0 0 4.8 $ Aluminium Porte-cible
6561  57 RCC  13.6 0 0 1.4 0 0 1.8 $ Vide dans le porte-cible
6562  57 RCC  15 0 0 1.5 0 0 2.5 $ Aluminium Porte-cible
6563  57 RCC  15 0 0 1.5 0 0 1.8 $ Vide dans le porte-cible
6564  57 RCC  16.5 0 0 0.1 0 0 2.5 $ Backing en Cuivre
6565  57 RCC  15 0 0 1.7 0 0 2.75 $ Eau de refroidissement
6566  57 RCC  15 0 0 1.5 0 0 4.8 $ Aluminium Porte-cible
6567  57 RCC  16.5 0 0 0.3 0 0 3.1 $ Aluminium Porte-cible
6568  57 PY   -23 $ Hexagone acier
6569  57 PY   23 
6570  57 PZ   -23 
6571  57 PZ   23 
6572  57 P    0 1 -0.6 -23 
6573  57 P    0 1 0.6 23 
6574  57 RCC  0 12.7 12.7 5 0 0 1.5 $ Inside fission chamber
6575  57 RCC  0 12.7 12.7 5 0 0 1.75 $ Cyl. fission chamber
c ----- Englobant CANEL SUD -----
6578  57 RPP  -13.75 110.5 -56.75 56.75 -101 50 $ Englobant CANEL SUD
C ************************ C
C ***** CHARIOT T400 ***** C
C ************************ C
6601  581 RPP  -774.25 -772.75 -15 15 -6 -3.5 $ Support Moteur fixe
6602 581 RPP  -785.750  -784.250   -15.000   15.000     -6.000    -3.500  
6603 581 RPP  -801.750  -796.750   -15.000   15.000     -6.000    -3.500
6605 581 RCC  -799.250   -17.500     0.000 -217.800      0   0     1.200  $ Rails chariot - suite � un conflit avec le support C�ne la vis est supprim�e, la densit� dispath�e sur les guides      
6606 581 RCC  -799.250    17.500     0.000 -217.800      0   0     1.200         
6607 581 RCC  -779.250   -25.000     3.001    0     5.000    0     6.500  $ Capot Moteur fixe 
6608 581 RCC  -779.250   -20.000     3.001    0    13.250    0     6.500  $ Moteur fixe       
6609 581 RCC  -779.250    -6.750     3.001    0     6.750    0     2.000       
6610 581 RPP  -784.250  -774.250   -16.875   -9.875      3.001    15.000                        
6611 581 RCC  -774.250     0.000     0.000  -25.000      0   0     3.500        
6612 582 RPP    -9.250     9.250   -30.000   30.000      2.300     4.500  $ Plateau support moteur inf
6613 582 RPP    -9.250    30.750   -43.750  -30.000      2.300     4.500    
6614 582 RCC     3.950   -39.500    10.001   17.000      0   0     5.500  $ Moteur inf
6615 582 RPP    -9.250     9.250    -9.250    9.250      4.500    20.700  $ Base inf carr�e
6616 582 RPP     9.250    23.750    -2.000   29.000     12.500    13.500  $ Plaque support moteur inf+
6617 582 RCC    19.250     9.500    19.001    0    17.000    0     5.500  $ Moteur inf+
6618 583 RCC     0.000     0.000     0.000    0   0      2.000     9.250  $ Plateau tournant
6619 583 RCC     0.000     0.000     2.000    0   0      2.000     9.500       
6620 583 RPP     6.450    32.950   -18.500   18.500      4.000     5.500  $ Plaque support moteur sup
6621 583 RPP   -12.050    11.950   -12.000   12.000      5.500     7.000  $ Plaque support detecteur inf
6622 583 RPP    11.950    13.450    10.500   14.500      5.500    14.500  $ Plateau Moteur sup
6623 583 RPP    31.450    32.950    10.500   14.500      5.500    14.500     
6624 583 RPP    13.450    31.450    -8.000   15.000     10.500    12.000   
6625 583 RCC    22.950     0.000    17.501    0    17.000    0     5.500  $ Moteur sup
6626 583 RCC     6.450     0.000     4.000    0   0      1.500    18.500  $ Coupe 6620 pour tourner
6627 583 RCC     6.450     0.000     5.500    0   0      1.500    18.500  $ Coupe 6621 pour tourner
6628 583 PX      6.450
6629 583 RPP   -12.000    12.000   -12.000   12.000     21.000    24.000  $ Porte-d�tecteur position basse
6630 583 RCC    -7.500    -7.500     7.000    0   0     14.000     1.000  $ Pieds
6631 583 RCC    -7.500     7.500     7.000    0   0     14.000     1.000  
6632 583 RCC     7.500    -7.500     7.000    0   0     14.000     1.000  
6633 583 RCC     7.500     7.500     7.000    0   0     14.000     1.000
6634  583 RPP  -12 12 -12 12 72.8 74.3 $ Porte-d�tecteur en position sur�lev�e
6635  583 RCC  -9 -9 24 0 0 48.8 1 $ H pieds = RPP (-Z) -24cm
6636  583 RCC  -9 9 24 0 0 48.8 1 $
6637  583 RCC  9 -9 24 0 0 48.8 1 
6638  583 RCC  9 9 24 0 0 48.8 1 
6639 583 RCC     0.000     0.000    21.000    0   0      3.000    14.999  $ Coupe Porte-d�tecteur bas 
6640  583 RCC  0 0 72.8 0 0 1.5 14.999 $ Coupe Porte-d�tecteur haut
c ----- Pupitre (AMANDE) -----
6641 584 RPP    -4.000     4.000   -4.000     4.000      0.000   106.000  $ pied pupitre
6642 584 RPP    -3.500     3.500   -3.500     3.500      0.500   105.500  $ air dans pied pupitre
6643 584 RPP   -15.800    15.800  -20.300    20.000    106.000   109.300  $ plateau pupitre
6644 584 RPP   -15.500    15.500  -20.000    20.000    106.300   123.000  $ �quipement pupitre
6645 584 RPP   -15.800    15.800  -20.300    20.300      0.000   123.000  $ Englobant pupitre
C ************************************* C
C ***** CHARIOT VAN GOGH - AVANC� ***** C
C ************************************* C
6701 591 RPP  -305.500   -20.500    -7.500     7.500   200.100   208.100   $ Module d'entrainement
6702 591 RPP  -297.500   -28.500    -6.000    -3.000   205.900   208.100   $ Logements vis sans fin
6703 591 RPP  -297.500   -28.500     3.000     6.000   205.900   208.100   
6704 591 RCC  -297.500    -4.500   207.000   269.000     0   0     1.000   $ Vis sans fin
6705 591 RCC  -297.500     4.500   207.000   269.000     0   0     1.000
6706 591 RPP   -20.500   -19.000    -7.500     7.500   200.100   209.100   $ But� face avt
6707 591 RPP   -19.000    -8.000    -4.700     4.700   200.100   208.100   $ Cache avt
6708 591 RPP   -19.000    -8.000    -4.500     4.500   200.100   207.900
6709 592 RPP   -71.500   -29.000   -18.750    18.750   210.500   213.500  $ Plaque basse
6710 592 RCC   -33.000   -13.500   213.500     0   0    27.500     2.500  $ Tiges
6711 592 RCC   -33.000    13.500   213.500     0   0    27.500     2.500  
6712 592 RCC   -62.500   -11.000   213.500     0   0    27.500     2.500  
6713 592 RCC   -62.500    11.000   213.500     0   0    27.500     2.500  
6714 593 RCC   -32.000     0.000   212.500     0   0    48.500     1.250  $ Tige guidage
6715 592 RPP   -71.500   -10.000   -18.750    18.750   241.000   244.000  $ Plaque haute
6716 592 RPP   -21.000   -10.000   -18.750    -8.000   241.000   244.000  $ Air Plaque haute
6717 592 RCC   -32.000     0.000   244.000     0   0    13.000     4.000  $ Guidage chariot
6718 592 RCC   -32.000     0.000   244.000     0   0    13.000     2.000  $ Air Guidage chariot
6719 592 RPP   -21.000   -17.000    -2.000     2.000   210.000   244.000  $ Carter verin
6720 592 RPP   -20.800   -17.200    -1.800     1.800   210.200   244.000  $ Air Carter verin
6721 592 RPP   -71.500   -37.000    18.750    19.050   213.500   244.000  $ Plaque +Y
6722 592 RPP   -71.500   -37.000   -19.050   -18.750   213.500   244.000  $ Plaque -Y
6723 593 RPP   -34.000   -10.000    -8.000     8.000   261.000   262.200  $ Plateau verin
6724 593 RPP   -28.000   -10.750     1.350     3.350   257.000   261.000  $ Support plateau verin +Y
6725 593 RPP   -28.000   -10.750    -3.350    -1.350   257.000   261.000  $ Support plateau verin -Y
6726 592 RPP   -27.500   -10.500    -5.500     5.500   244.000   247.300  $ Support moteur
6727 592 RCC   -19.000     0.000   247.300     0   0     6.200     5.000  $ Gros Cyl
6728 593 RCC   -19.000     0.000   212.200     0   0    43.700     1.200  $ Verin
6729 593 RCC   -19.000     0.000   255.900     0   0     4.600     2.000  $ Chape tige verin
6730 592 RCC   -15.400    -5.500   249.640     0    11.000   0     2.830  $ Verin moteur
6731 592 RCC   -15.400   -10.670   249.640     0     5.170   0     3.290  
6732 592 RCC   -15.400   -13.350   249.640     0     2.680   0     5.250  $ Bride
6733 592 RCC   -15.400   -23.000   249.640     0     9.650   0     4.210  $ Moteur
6734 594 RPP   -31.000    -7.000   -12.000    12.000   270.600   272.500  $ Plateau table tournante
6735 594 RCC   -19.000     0.000   270.600     0   0     1.900    15.250   
6736 594 RCC   -19.000     0.000   269.600     0   0     1.000     3.750   
6737 594 RCC   -19.000     0.000   269.600     0   0     2.900     1.500  $ Air Plateau table tournante
6738 594 RPP   -34.000    -4.000   -15.000    15.000   272.500   275.000  $ Rehausse
6739 594 RCC   -19.000     0.000   272.000     0   0     3.000    15.250   
6740 594 RPP   -34.000   -31.000    -7.000     7.000   272.000   272.500   
6741 594 RPP    -7.000    -4.000    -7.000     7.000   272.000   272.500   
6742 594 RPP   -26.000   -12.000   -15.000   -12.000   272.000   272.500   
6743 594 RPP   -26.000   -12.000    12.000    15.000   272.000   272.500   
6744 594 RCC   -29.000     0.000   275.000     0   0    25.500     1.000  $ Tiges rehausse
6745 594 RCC   -14.000     8.660   275.000     0   0    25.500     1.000   
6746 594 RCC   -14.000    -8.660   275.000     0   0    25.500     1.000   
6747 594 RPP   -34.000    -4.000   -15.000    15.000   300.500   302.000  $ Plateau
6748 594 RCC   -19.000     0.000   300.500     0   0     1.500    15.250   
6749 594 RCC    -9.000     0.000   275.000     0   0     1.900     1.150  $ Bouchons
6750 594 RCC   -24.000     8.660   275.000     0   0     1.900     1.150   
6751 594 RCC   -24.000    -8.660   275.000     0   0     1.900     1.150   
6752 594 RCC    -9.000     0.000   276.900     0   0     1.300     2.400   
6753 594 RCC   -24.000     8.660   276.900     0   0     1.300     2.400   
6754 594 RCC   -24.000    -8.660   276.900     0   0     1.300     2.400   
6755 593 RPP   -27.000   -11.000    -8.000     8.000   262.200   268.200  $ Aerotech
6756 593 RCC   -22.000   -13.000   265.200     0    5.000    0     2.000  $ Moteur
6757 591 RCC  -320.500     0.000   204.100    15.000     0   0     1.000  $ Moteur fixe - tige
6758 591 RPP  -324.500  -320.500    -2.000     7.500   200.100   206.100  $ Moteur fixe - support
6759 591 RCC  -322.500     2.250   206.100     0   0    15.000     5.000  $ Moteur fixe
6760 592 RPP  -176.500   -71.500     8.500    17.000   207.500   210.500  $ Chaine + Cablage
6761 592 RPP  -176.500   -71.500     8.500    17.000   238.000   241.000   
6762 592 RCC  -176.500     8.500   224.250     0    8.500    0    13.750   
6763 592 RCC  -176.500     8.500   224.250     0    8.500    0    16.750   
6764 592 PX   -176.500
C *************************************
C ***** BLOC SOURCE VAN GOGH - Cf *****
C *************************************
c Sources Container - Polyethilen and Polyurethan Box
7001  RPP  -37.8 37.8 -34.8 47.8 30.3 105.6 $ Polyurethan ext
7002  RPP  -37.5 37.5 -34.5 47.5 30.3 105.3 $ Polyethilen int
7003  RCC  0 0 30.4 0 0 75.2 4.75 $ cavit� Cf
7004  RCC  0 13 30.4 0 0 75.2 4.75 $ cavit� Am-Be
7005  RPP  -11 11 -13.5 26.5 20.3 30.3 $ Polyethilen bottom block
c Tubes support
7006  RPP  -12.5 12.5 -16.4 29 105.6 106.6 $ top plaque
7007  RCC  0 0 30.4 0 0 75.7 4.445 $ tube Cf
7008  RCC  0 13 30.4 0 0 75.7 4.445 $ tube Am-Be
7009  RCC  0 0 35.7 0 0 70.4 3.896 $ air tube Cf
7010  RCC  0 13 35.7 0 0 70.4 3.896 $ air tube Am-Be
7011  RCC  0 0 106.1 0 0 0.5 4.445 $ air top tube Cf
7012  RCC  0 13 106.1 0 0 0.5 4.445 $ air top tube Am-Be
c Fixed Source Supports
7013  RCC  0 0 30.4 0 0 5.3 4.05 $ bottom part Cf
7014  RCC  0 0 35.7 0 0 2 3.1 $ intermediate part Cf
7015  RCC  0 0 37.7 0 0 3 1.5 $ upper part Cf
7016  RCC  0 0 30.4 0 0 10.3 0.9 $ air source Supports Cf
7017  RCC  0 13 30.4 0 0 5.3 4.05 $ bottom part Am-Be
7018  RCC  0 13 35.7 0 0 2 3.1 $ intermediate part Am-Be
7019  RCC  0 13 37.7 0 0 3 1.5 $ upper part Am-Be
7020  RCC  0 13 30.4 0 0 10.3 0.9 $ air source Supports Am-Be
c Ejection tube and air volume Cf
7021  RCC  0 0 36.3 0 0 257.6 3.5 $ ejection tube Cf
7022  RCC  0 0 36.3 0 0 257.6 3.2 $ air Ejection tube Cf
7023  RCC  0 0 106.6 0 0 1.5 6.5 $ inf upper support
7024  RCC  0 0 108.1 0 0 3.5 4.25 $ sup upper support
c Stopper tube Am-Be
7025  RCC  0 13 106.6 0 0 5 5.5 $ top part
7026  RCC  0 13 75.6 0 0 31 3.8 $ inside part
c Cf Porte-source
7027  RCC  0 0 287.9375 0 0 13.5 3.1 $ piston Cf
7099  RCC  0 0 287.9375 0 0 3 1.5 $ Air piston Cf
7028  RCC  0 0 297.5875 0 0 3.85 0.4 $ Base porte source inf
7029  RCC  0 0 301.4375 0 0 8.05 0.5 $ Base porte source sup
7030  RCC  0 0 309.4875 0 0 2 0.5 $ Meplat serrage
7031  PY   -0.4 
7032  PY   0.4 
7033  RCC  0 0 311.4875 0 0 4 0.5 $ Base porte source sup
7034  RCC  0 0 313.4875 0 0 3 0.3 $ Reglages inf
7035  RCC  0 0 316.4875 0 0 1 0.523 $ Reglages milieu
7036  RCC  0 0 317.4875 0 0 2 0.45 $ Reglages sup
7037  RCC  0 0 317.4875 0 0 3.2 0.55 $ Coiffe
7038  RCC  0 0 319.4875 0 0 1.015 0.4 $ Air Coiffe
7039  RCC  0 0 320.6875 0 0 0.6 0.5 $ Top Coiffe
c Cf source
7040  RCC  0 0 319.785 0 0 0.43 0.16 $ Cf source
7041  RCC  0 0 319.785 0 0 0.43 0.215 $ 6A Spacer
7042  RCC  0 0 319.705 0 0 0.7 0.3 $ Cell body
7043  RCC  0 0 319.785 0 0 0.62 0.22 $ air Cell body
7044  RCC  0 0 320.225 0 0 0.18 0.22 $ Cell lid
7045  RCC  0 0 320.305 0 0 0.1 0.155 $ air Cell lid
7046  RCC  0 0 319.7 0 0 0.005 0.25 $ 07 Spacer
7047  RCC  0 0 319.51 0 0 0.19 0.31 $ Sheath lid
7048  RCC  0 0 319.51 0 0 0.1 0.245 $ air Sheath lid
7049  RCC  0 0 319.51 0 0 0.98 0.375 $ Sheath body
7050  RCC  0 0 319.51 0 0 0.9 0.31 $ air Sheath body
c Cf sphere
7051  SZ   320 15.08 $ sphere
7052  SZ   320 15 $ D2O sphere
7053  RCC  0 0 304.22 0 0 32.2 0.65 $ tube dans sphere
7054  RCC  0 0 322.02 0 0 1.2 0.65 $ bouchon dans tube
7055  RCC  0 0 336.42 0 0 0.9 1.55 $ bouchon sup
7056  RCC  0 0 337.32 0 0 1.3 1.85 
7057  RCC  0 0 302.47 0 0 3 1.25 $ support inf
7058  RCC  0 0 302.47 0 0 33.95 0.6 $ air tube
7059  RCC  0 0 300.6 0 0 5.5 5.715 $ support sphere
7060  RCC  0 0 299.7 0 0 0.9 7.5 $ bride
7061  RCC  0 0 298.8 0 0 0.9 7.5 $ bride tube D=114.3
7062  RCC  0 0 197.9 0 0 100.9 5.715 $ tube D=114.3
7063  RCC  0 0 197.9 0 0 108.2 5.41 $ air tube D=114.3
7064  RPP  -12.815 12.815 -1.125 1.125 199.4 200.9 $ pattes tube D=114.3
7065  RPP  -1.125 1.125 -12.815 12.815 199.4 200.9 
7066  RCC  -11.5 0 195.9 0 0 3.5 1.125 $ pieds
7067  RCC  11.5 0 195.9 0 0 3.5 1.125 
7068  RCC  0 -11.5 195.9 0 0 3.5 1.125 
7069  RCC  0 11.5 195.9 0 0 3.5 1.125 
c Poutre sur ejection tube
7070  RPP  -61.2 126 -14 14 179.6 194.6 $ poutre
7071  RPP  -61.2 126 -13.6 13.6 179.6 194.2 $ air int poutre
7072  RPP  -3.6 3.6 -14 0 179.6 195.9 $ passage ejection tube
7073  RCC  0 0 194.2 0 0 1.7 3.6 $ passage ejection tube
7074  RPP  -61.2 -27.2 -3 3 194.2 194.6 $ fente -X
7075  RPP  98 126 -14 14 194.6 196.1 $ plaque +X
7076  RPP  -14 14 -14 14 194.6 195.9 $ plaque +Z
7077  RPP  -27.2 32.8 14 19 183.6 193.6 $ platine +Y
7078  RPP  -27.2 32.8 14 18.6 184 193.2 $ air platine +Y
7079  RPP  103.486 113.486 -13.6 13.6 189.7 194.2 $ platine inf
c Cadmium sphere
7080  SZ   320 15.16 $ Cd sphere
c Chassis
7081  RPP  -39 39 -66.5 56.5 14.9 24.9 $ chassis Bloc source
7082  RPP  -34 34 -61.5 51.5 14.9 24.9 $ air chassis Bloc source
7083  RPP  -2.5 2.5 -61.5 51.5 14.9 24.9 $ renfort chassis Bloc source
7084  RCC  -30.8 -27.8 24.9 0 0 5.4 8 $ pied bloc
7085  RCC  30.8 -27.8 24.9 0 0 5.4 8 
7086  RCC  -30.8 40.8 24.9 0 0 5.4 8 
7087  RCC  30.8 40.8 24.9 0 0 5.4 8 
7088  RPP  -4.2 37.8 -63.5 -41.5 41.9 44.9 $ support armoire elec
7089  RPP  -1.2 34.8 -60.5 -44.5 41.9 44.9 $ air support armoire elec
7090  RPP  -4.2 -1.2 -63.5 -60.5 24.9 41.9 $ pieds
7091  RPP  34.8 37.8 -63.5 -60.5 24.9 41.9 
7092  RPP  -4.2 -1.2 -44.5 -41.5 24.9 41.9 
7093  RPP  34.8 37.8 -44.5 -41.5 24.9 41.9 
7094  RPP  -3.2 36.8 -62.5 -42.5 44.9 104 $ armoire elec
7095  RCC  -37 -59 7.45 3.5 0 0 7.45 $ roues
7096  RCC  -37 49 7.45 3.5 0 0 7.45 
7097  RCC  33.5 -59 7.45 3.5 0 0 7.45 
7098  RCC  33.5 49 7.45 3.5 0 0 7.45 
c Stocked source Am-Be
C ----- suite aux informations non-disponibles, la source est celle du fichier Van_Gogh.i fourni -----
7101  RCC  0 13 37.7 0 0 13.5 3.1 $ piston Am-Be
7102  RCC  0 13 51.2 0 0 18.85 0.5 $ tige support
7103  RCC  0 13 51.2 0 0 18.85 1.785 $ esp. air/tige support
7104  RCC  0 13 58.25 0 0 11.7 1.945 $ partie inf.tube dural
7105  RCC  0 13 69.95 0 0 4.43 1.875 $ capot tube dural
7108  RCC  0 13 69.95 0 0 4.43 1.945 $ air capot tube dural
7109  RCC  0 13 70.05 0 0 1 1.55 $ support source
7110  RCC  0 13 70.55 0 0 3 1.5 $ capsule source
7111  RCC  0 13 70.95 0 0 2.2 1.1 $ zone active Am-Be
7112  RCC  0 13 70.05 0 0 3.55 1.6 $ capot maintien source
7113  RCC  0 13 71.05 0 0 2.5 1.55 $ espace d'air
7114  RCC  0 13 70.05 0 0 4.01 1.785 $ espace air sup. capot
7115  RCC  0 13 64.68 0 0 9.8 2.045 $ ecran plomb ep. 1mm
7120  RPP  -39 39 -66.5 56.5 0 173.5 $ englobant sous poutre
c ----- Englobants sous poutre & poutre -----                           
7121  RPP  -27.2 126 -14 19 179.6 196.1 $ englobant poutre
C --- Detecteur-Berthold
100   CZ   0.0025 $wire
101   PZ   2 $wire top
102   PZ   -2 $wire bottom
103   CZ   1.9 $3He tube_gaschamber
104   PZ   -4.57 $down horn ceramic insulator
105   CZ   0.92 $down horn ceramic insulator
106   PZ   -5 $down field ceramic insulator
107   PZ   4.57 $top horn ceramic insulator
108   PZ   5 $top field ceramic insulator
109   PZ   6 $inner ceramic plug
110   CZ   0.98 $inner ceramic plug
111   CZ   2 $3He tube_covershield
112   PZ   -6.96 $down cadmium cylinder
113   PZ   7.45 $up cadmium cylinder
114   CZ   4.089 $Cd cylinder absorber in
115   CZ   4.189 $Cd cylinder absorber out
116   PZ   13.764 $cable cavity
117   PZ   11.75 $down SS detector ring
118   PZ   13.033 $down SS detector ring
119   CZ   2.45 $down SS detector ring
120   CZ   3.063 $up SS detector ring
121   RCC  8.5 -8.5 0 -10 10 0 0.35 $rovina XY, vpravo dole
122   RCC  8.5 8.5 0 -10 -10 0 0.35 $rovina XY, vpravo hore
123   RCC  -8.5 -8.5 0 10 10 0 0.35 $rovina XY, vlavo dole
124   RCC  -8.5 8.5 0 10 -10 0 0.35 $rovina XY, vlavo hore
125   RCC  8.5 0 -8.5 -9 0 9 0.35 $rovina XZ, vpravo dole
126   RCC  8.5 0 8.5 -9 0 -9 0.35 $rovina XZ, vpravo hore
127   RCC  -8.5 0 -8.5 9 0 9 0.35 $rovina XZ, vlavo dole
128   RCC  -8.5 0 8.5 9 0 -9 0.35 $rovina XZ, vlavo hore
129   RCC  0 8.5 -8.5 0 -9 9 0.35 $rovina YZ, vpravo dole
130   RCC  0 8.5 8.5 0 -9 -9 0.35 $rovina YZ, vpravo hore
131   RCC  0 -8.5 -8.5 0 9 9 0.35 $rovina YZ, vlavo dole
132   RCC  0 -8.5 8.5 0 9 -9 0.35 $rovina YZ, vlavo hore
133   SO   11.5 $inner PE sphere
134   SO   12.5 $outer PE sphere
135   SO   30 $outer space

C *************************************************************************** C
C ******************************* TRANSLATIONS ****************************** C
C *************************************************************************** C
C --------------------------------------------------------------------------- C
C ------- Les TR1, TR2 et TR3 des vrais positions des diodes C, A et B ------ C
C -------    pour affichage SuperMC, les rotations sont � supprimer    ------ C
C --------------------------------------------------------------------------- C
C
C SuperMC TR1 -712.8619  345.7500   237.7482   1 0 0  0 1 0  0 0 1   $ Diode C
C SuperMC TR2 -712.8619  339.0399   226.1259   1 0 0  0 1 0  0 0 1   $ Diode A
C SuperMC TR3 -712.8619  352.4601   226.1259   1 0 0  0 1 0  0 0 1   $ Diode B
TR1 -712.8619  345.7500   237.7482   0.9961947  0.0000000 -0.0871557  &     
                                     0.0000000  1.0000000  0.0000000  &     
                                     0.0871557  0.0000000  0.9961947 $ Diode C
TR2 -712.8619  339.0399   226.1259   0.9961892  0.0754788  0.0437029  &
                                    -0.0491614  0.0720427  0.9961892  &
                                     0.0720427 -0.9945415  0.0754788 $ Diode A
TR3 -712.8619  352.4601   226.1259   0.9961892 -0.0754788  0.0437029  &
                                     0.0491614  0.0720427 -0.9961892  &
                                     0.0720427  0.9945415  0.0754788 $ Diode B
C --------------------------------------------------------------------------- C
C ------------------------ Positionnement BLOG (TR56) ----------------------- C
C --------------------------------------------------------------------------- C
TR56 -933.7 273.75 0 1 0 0 0 1 0 0 0 1 $ BLOG sur le banc T400 - RETRAIT
C --------------------------------------------------------------------------- C
C ----------------------- Positionnement CANEL (TR57) ----------------------- C
C --------------------------------------------------------------------------- C
TR57 139.5 345.75 101 1 0 0 0 1 0 0 0 1 $ CANEL hors banc T400 - SUD
C --------------------------------------------------------------------------- C
C ---------------- Positionnement Chariot T400 (TR582-TR583) ---------------- C
C --------------------------------------------------------------------------- C
TR581 508.55 345.75 135 1 0 0 0 1 0 0 0 1 $ El�ments fixes du Chariot T400 - NE PAS MODIFIER
C --------------------------------------------------------------------------- C
C ----------                   !!! ATTENTION !!!                   ---------- C
C --------------------------------------------------------------------------- C
C ---- 1. TR582 et TR583 varient ensemble en X entre -300.0 (RECUL�)     ---- C
C ----    et -499.3 (AVANC�). Ces X correspondent au centre du plateau   ---- C
C ---- 2. Dans le cas d'une rotation, elle est � ajouter � TR583         ---- C
C ---- 3. La hauteur du plateau est ajustable en fonction de la taille   ---- C
C ----    du d�tecteur via les surfaces 6634 6635 6636 6637 6638 6640    ---- C
C ----    Par d�faut, la surface sup�rieure du plateau est � Z=+230cm    ---- C
C --------------------------------------------------------------------------- C
TR582 -300 345.75 135 1 0 0 0 1 0 0 0 1 $ Chariot T400 - Partie mobile RECULE (D�faut)C INCA [CHARIOT T400 RECULE]
TR583 -300 345.75 155.7 1 0 0 0 1 0 0 0 1 $ Chariot T400 - Partie tournante RECULE (D�faut)C INCA [CHARIOT T400 RECULE]
C 
C
C --------------------------------------------------------------------------- C
C ---------------------- Positionnement Pupitre (TR584) --------------------- C
C --------------------------------------------------------------------------- C
TR584 -260.00 260.00 0.0 1 0 0 0 1 0 0 0 1  $ Position arbitrare du Pupitre c�t� banc T400
C
C --------------------------------------------------------------------------- C
C -------------- Positionnement Chariot Van Gogh (TR592-TR594) -------------- C
C --------------------------------------------------------------------------- C
TR591 0 0 0 1 0 0 0 1 0 0 0 1 $ El�ments fixes du Chariot Van Gogh - NE PAS MODIFIER
C --------------------------------------------------------------------------- C
C ----------                   !!! ATTENTION !!!                   ---------- C
C --------------------------------------------------------------------------- C
C ---- 1. En position avanc�e "th�orique" (axe chariot � 19cm de l'axe   ---- C
C ----    de la source Cf) il y a des conflits entre la rehausse (6738)  ---- C
C ----    et le tube D=114.3 de la sphere (7059-7062) et entre le        ---- C
C ----    plateau des d�tecteurs (6747) et la sphere (7080, 7051, 7052)  ---- C
C ----    ALORS la distance minimale "r�elle" est de X = 30.2cm          ---- C
C ---- 2. TR592 TR593 TR594 varient ensemble en X entre -245.7 (RECUL�)  ---- C
C ----    et -11.2 (AVANC�)                                              ---- C
C ----    Le centre X de la rehausse (et du plateau) sera � -264.7cm  et ---- C
C ----    � -30.2cm respectivement                                       ---- C
C ---- 3. Par d�faut, en position basse, la surface sup�rieure du        ---- C
C ----    plateau est � Z=+275cm et celle de la rehausse est � Z=+302cm  ---- C
C ----    - Si la distance entre le bas du d�tecteur (y compris son      ---- C
C ----    support �ventuel) est la ligne du faisceau (+320 cm) est       ---- C
C ----    inf�rieure � 18 cm, alors la hauteur plateau+rehasse est g�r�e ---- C
C ----    via la position Z � ajouter aux TR593 et TR594 (de 0 � 32 cm)  ---- C
C ----    - Si celle-ci est sup�riere � 18 cm, la rehausse (6738 6740    ---- C
C ----    6744 6747 6749) doit �tre supprim�e du mod�le et un autre      ---- C
C ----    "ins�r�" de type "Support" + la position Z des TR593 et TR594  ---- C
C ----    peuvent �tre utilis�s pour ajuster la hauteur du d�tecteur     ---- C             
C ---- 4. Dans le cas d'une rotation, elle est � ajouter � TR594         ---- C
C --------------------------------------------------------------------------- C
TR592 -56 0 0 1 0 0 0 1 0 0 0 1 $ -131 = -150 cm : Chariot VG - Partie mobile RECULE (D�faut)C INCA [CHARIOT VG RECULE]
TR593 -56 0 5.5 1 0 0 0 1 0 0 0 1 $ -131 = -150 cm : TR592 + Partie montante RECULE+BASSE (D�faut)C INCA [CHARIOT VG RECULE]
TR594 -56 0 5.5 1 0 0 0 1 0 0 0 1 $ -131 = -150 cm : TR593 + Partie tournante RECULE+BASSE+0� (D�faut)C INCA [CHARIOT VG RECULE]
TR401 -75   0 320 1 0 0 0 1 0 0 0 1 $ Berthold translation
C
C
C --------------------------------------------------------------------------- C
C --------------- Positionnement Ins�r�s (N� TR g�r�s par INCA) ------------- C
C --------------------------------------------------------------------------- C
C -----                        !!! ATTENTION !!!                        ----- C
C --------------------------------------------------------------------------- C
C ---- 1. Les CONES D'OMBRE sont mod�lis�s avec la face avant vers +Y    ---- C
C ----    Une rotation de +90� (0 1 0  -1 0 0  0 0 1) est n�cessaire     ---- C
C ----    pour placer un cone sur le banc T400 + Translation Z=-490cm.   ---- C
C ----    Une rotation de -90� (0 -1 0  1 0 0  0 0 1) est n�cessaire     ---- C
C ----    pour placer un cone sur le banc VG + Translation Z=-400cm.     ---- C
C ---- 2. La face avant des d�tecteurs �TPC, PLC, BC501A, BSS-passif est ---- C
C ----    orient�e vers +X. Ces d�t�cteurs doivent �tre tourn�s � 180�   ---- C
C ----    (-1 0 0  0 -1 0  0 0 1) lorsqu'ils sont sur le banc T400       ---- C
C ----    ATTENTION � la distance du d�tecteur par rapport � la source   ---- C
C ---- 3. La face "active" du Fant�me ICRU est  orient�e vers -X.        ---- C
C ----    Le Fant�me doit �tre tourn� � 180� (-1 0 0  0 -1 0  0 0 1)     ---- C
C ----    lorsqu'il est sur le banc Van Gogh                             ---- C
C ----    ATTENTION � la distance du d�tecteur par rapport � la source   ---- C
C --------------------------------------------------------------------------- C
C
C
C
C --------------------------------------------------------------------------- C
C -----                        SOURCES ET PHYSIQUE                      ----- C
C --------------------------------------------------------------------------- C
mode  n h t d s
cut:h,t j 1e-3                                                                  
phys:n 6j 4 
c
C ----------------------------------------------------------------------------
C ----  Cf252 ----------------------------------------------------------------
C ----------------------------------------------------------------------------
SDEF CELL=7040 POS=0 0 319.785 AXS=0 0 1 ERG=D1 EXT=D2 RAD=D3 PAR=N
C ERG ----- A MODIFIER -----
SI1 H   0  4.223E-9 1.334E-8 4.212E-8 1.330E-7 4.201E-7 &
           1.327E-6 4.190E-6 1.323E-5 4.179E-5 1.320E-4 &
           4.168E-4 1.316E-3 4.158E-3 1.313E-2 4.147E-2 &
           1.171E-1 3.204E-1 5.236E-1 7.269E-1 9.302E-1 &
           1.133E+0 1.337E+0 1.540E+0 1.743E+0 1.947E+0 &
           2.150E+0 2.353E+0 2.556E+0 2.760E+0 2.963E+0 &
           3.166E+0 3.370E+0 3.573E+0 3.776E+0 3.979E+0 &
           4.183E+0 4.386E+0 4.589E+0 4.793E+0 4.996E+0 &
           5.199E+0 5.402E+0 5.606E+0 5.809E+0 6.012E+0 &
           6.215E+0 6.419E+0 6.622E+0 6.825E+0 7.029E+0 &
           7.232E+0 7.435E+0 7.638E+0 7.842E+0 8.045E+0 &
           8.248E+0 8.452E+0 8.655E+0 8.858E+0 9.061E+0 &
           9.265E+0 9.468E+0 9.671E+0 9.875E+0 1.008E+1 &
           1.028E+1 1.048E+1 1.069E+1 1.089E+1 1.100E+1
SP1 D   0 3.837E-10 3.351E-9 1.290E-8 4.441E-8 1.348E-7 &
           3.602E-7 9.684E-7 2.605E-6 7.023E-6 1.902E-5 &
           5.205E-5 1.450E-4 4.255E-4 1.390E-3 5.273E-3 &
           1.631E-2 3.750E-2 3.314E-2 2.878E-2 2.394E-2 &
           2.045E-2 1.776E-2 1.576E-2 1.684E-2 1.884E-2 &
           2.075E-2 2.188E-2 2.074E-2 2.157E-2 2.639E-2 &
           3.326E-2 3.518E-2 2.985E-2 3.108E-2 2.985E-2 &
           2.750E-2 2.735E-2 2.772E-2 2.928E-2 3.229E-2 &
           3.112E-2 2.831E-2 2.468E-2 2.306E-2 2.036E-2 &
           1.587E-2 1.777E-2 1.724E-2 1.566E-2 1.447E-2 &
           1.326E-2 1.431E-2 1.583E-2 1.439E-2 1.367E-2 &
           1.224E-2 8.957E-3 6.351E-3 3.792E-3 2.910E-3 &
           3.047E-3 4.127E-3 5.666E-3 5.705E-3 5.960E-3 &
           4.504E-3 3.080E-3 1.688E-3 6.312E-4 2.259E-5
C EXT
SI2 0 0.43
SP2 0 1
C 
C RAD
SI3 0 0.16
SP3 -21 1
c
c
C ----------------------------------------------------------------------------
C ------------------------- DEFINITION DES TALLIES ---------------------------
C ----------------------------------------------------------------------------
c ATTENTION ATTENTION - ATTENTION - ATTENTION - ATTENTION - ATTENTION ATTENTION
c ATTENTION ATTENTION - ATTENTION - ATTENTION - ATTENTION - ATTENTION ATTENTION
c ATTENTION                                                           ATTENTION
c ATTENTION   !!!   A REINSEGNER MANUELLEMENT SELON LE BESOIN   !!!   ATTENTION
c ATTENTION                                                           ATTENTION
c ATTENTION ATTENTION - ATTENTION - ATTENTION - ATTENTION - ATTENTION ATTENTION
c ATTENTION ATTENTION - ATTENTION - ATTENTION - ATTENTION - ATTENTION ATTENTION
c
c --------------------                                                          
c TALLY                                                                         
c --------------------    
fc6 ed_proton                                                      
f6:h 101                                                                          
fc16 ed_triton                                                      
f16:t 101                                                                         
fc26 ed_deuteron                                                      
f26:d 101
fc36 ed_helion                                                      
f36:s 101                                                                       
fc8 resp6                                                      
f8:n 101                                                                          
ft8 phl 4 6 1 16 1 26 1 36 1 0                                                               
E8 0 0.190 0.785 NT $ whole spectrum, from tritium edge
c EM8 490.8738521 490.8738521 490.8738521 $ multiplicator, surface of detector 12.5cm
C T8 0 1E4 NT $ time of pulse       
c --------------------                                                          
fc4 resp4                                                      
f4:n 101 104 105 $active volume of 3He tube                                                                          
c -------------------- 
c 3.5 bar = 3.45 atm, N(He-3) = 8.64757E-5 atoms/b-cm.       
c ro (He-3) = N�M/N_A  = 4.3309E-4 g /cm3                                                    
c volume detector = 45.3645 (89.9905)                                                         
c multiplication factor = 2.47585326 (3.819978786)                                           
c plocha zvazku = 490.8738521                                                    
c density  =1.111831E-04 3He+CH4 (8.647576E-5 only 3He)  
C FM4--- Taux reaction np/cm3 --> cm2 si  Multiplication factor = (pi*SI1**2)*Vol.det*atomicdensity                                                           
c --------------------    
c E4 0 0.745 0.765 NT $ only peak of full absorbtion 765keV                                                      
c fm4 (3.819978786 2 103) (3.819978786 2 1) (3.819978786 2 2) $p mutliplicator for 3He+CH4 
fm4 (3.819978786 2 103)$p, mutliplicator for 3He+CH4 
c --------------------                                                          
C --------------------------------------------------------------------------- C
C -----                           RUN CONTROL                           ----- C
C --------------------------------------------------------------------------- C
rand GEN=2 SEED=19073486328125 STRIDE=152917 $ Gives fatal error on Vised - Number of histories: NPS * stride < 9.2E+18 instead of DEFAULT 7.04E+13 !$
prdmp j -10 1 4 $ dump 20 every minutes - write mctal - maximum number of dump written on runtpe file
lost 100
C stop CTME 30 nps 1E6 F8 0.01                                           
stop CTME 10 nps 1E8 F8 0.01  
C nps 1E8   
ptrac file=bin write=all $ Write PTRAC file
print  
c
C --------------------------------------------------------------------------- C
C -----                             MATERIAUX                           ----- C
C --------------------------------------------------------------------------- C
c     Tungsten, density = 18.35 g/cm3                                         
M1    26054.70c -0.001  26056.70c -0.009  28058.70c -0.022  28060.70c -0.008
      74182.70c -0.252  74183.70c -0.137  74184.70c -0.296  74186.70c -0.275
C ---------------------------------------------------------
c      3He+CH4, density = -0.001090816 g/cm3 (3.5bar3He+1barCH4)                                  
M2    2003.70c              -0.39686   $3He
      6012              -0.451570918  $C 74.87% of CH4
      1001.70c              -0.151569082  $H 25.13% of CH4
C ---------------------------------------------------------
c      Steatite ceramic (electrical insulators), density = -2.7 g/cm3           
c      crystalline form of magnesium5 silicate MgO - Al2O3 - SiO2 insulator               
M3    8016.70c      -0.440715  $ oxygen
      12024.70c     -0.391973  $ manganese
      13027.70c     -0.031755  $ aluminium
      14028.70c     -0.135556  $ silicon
C ---------------------------------------------------------
c     Stainless steel, density = -7.86 g/cm3 19.5% Cr    70.5% Fe    10%Ni                                                
M4    24052.70c  -0.174  24053.70c -0.021  26054.70c -0.042  
      26056.70c -0.663   28058.70c -0.072  28060.70c -0.028 
C ---------------------------------------------------------
c      Cadmiun, density = -8.65 g/cm3 $ but not perforated                      
M5    48106.70c -0.0125  48108.70c -0.0089  48110.70c -0.1249  48111.70c -0.128
      48112.70c -0.2413  48113.70c -0.1222  48114.70c -0.2873  48116.70c -0.0749
C ---------------------------------------------------------
c      PNNL-15870 Air Dry (sea level) density = -0.001225g/cm3                  
M6    6012  -0.000124  7014.70c -0.755268  8016.70c -0.231781 
      18036.70c -3.9e-005 18038.70c -8e-006    18040.70c -0.01278 
C ---------------------------------------------------------
c      StainlessSteel  AISI316LN, density = -7.8 g/cm3                          
M7    26000 -0.67145  24000 -0.185   28000 -0.1125 12000 -0.02 
      14000 -0.01     15031.70c -0.00045 16000 -0.0003  6012 -0.0003 
C ---------------------------------------------------------
c      Polyethylene / CH2 (H:2., C:1.) resp. C2H4 (H:4., C:2.)                  
M8    1001.70c                 4  $ PE LB 6411
      6000.70c                 2       
MT8     poly.10t            $ detailed material card for 20�CPRINT
C --------------------------------------------------------------------------- C
C -----                             MATERIAUX                           ----- C
C --------------------------------------------------------------------------- C
C  - Dalle et Plots - B�ton AMANDE (article MP) commun + 100 kg/m3 Acier (d=2.4)
M11   1001.60c   -0.00621    & $ H
      6000.60c   -0.06119    & $ C
      7014.60c   -0.00191    & $ N
      8016.60c   -0.43973    & $ O
     12000.60c   -0.00621    & $ Mg
     13027.60c   -0.01625    & $ Al
     14000.60c   -0.11513    & $ Si
     15031.60c   -0.00002    & $ P
     16000.60c   -0.00164    & $ S
     19000.60c   -0.00382    & $ K
     20000.60c   -0.29634    & $ Ca
     22000.60c   -0.00080    & $ Ti
     24000.42c   -0.00713    & $ Cr
     25055.60c   -0.00125    & $ Mn
     26000.42c   -0.03556    & $ Fe
     28000.42c   -0.00504    & $ Ni
     30000.40c   -0.00003    & $ Zn
     37085.66c   -0.00002    & $ Rb
     38088.70c   -0.00066    & $ Sr
     42000.60c   -0.00104      $ Mo
C ---------------------------------------------------------
C  - Air Dry, Near Sea Level - PNNL-15870 Rev. 1 + 0.0556% H1(d=1.300E-03)
M12   1001.60c   -0.000556   & $ H
      6000.60c   -0.000124   & $ C
      7014.60c   -0.754848   & $ N
      8016.60c   -0.231652   & $ O
     18000.42c   -0.012820     $ Ar
C ---------------------------------------------------------
C  - Panol�ne - compo prise �gale � celle de la laine de verre (d=0.04)
C http://www.cem2.univ-montp2.fr/~Hyg_Secur/autresqueamiante/physicochim.htm
C
M13  14000.60c   -60.000  & $ Si
     13027.60c   -3.500   & $ Al
     20000.60c   -6.432   & $ Ca
     12000.60c   -1.508   & $ Mg
     11023.60c   -11.499  & $ Na
     19000.60c   -1.038   & $ K
     26000.42c   -0.389   & $ Fe
      5010.60c   -0.461   & $ B10
      5011.60c   -1.868   & $ B11
     22000.60c   -0.150   & $ Ti
      8016.60c   -13.156    $ O
C ---------------------------------------------------------
C  - Poutres/Plateformes/Pont Roulant... - Acier de construction (d=7.8212)
M14  26000.42c  -99.0  & $ Fe
      6000.60c  -1.00    $ C
C ---------------------------------------------------------
C  - Aluminium bardage - PNNL-15870 Rev. 1 (d=2.6989)
M15  13027.60c   -1.000
C ---------------------------------------------------------
C -  Vitres - Verre PYREX (d=2.54)
M16   8016.60c  -54.0  & $ O
      5010.60c  -0.76  & $ B10
      5011.60c  -3.24  & $ B11
     11023.60c   -3.0  & $ Na
     13027.60c   -1.0  & $ Al
     14000.60c  -38.0    $ Si
C ---------------------------------------------------------
C -  Argile AMANDE (d=1.2)
M17   6000.60c  -0.09  & $ C
     14000.60c  -0.18  & $ Si
      8016.60c  -0.34  & $ O16
     26056.60c  -0.29  & $ Fe56
     12000.60c  -0.1     $ Mg
C ---------------------------------------------------------
C  - Blog - Graphite (d=1.693)
M18   6000.60c   -1.000
C ---------------------------------------------------------
C  - Blog - PEHD (d=0.93)
M19   1001.60c    0.66667    & $ H
      6000.60c    0.33333      $ C
MT19  poly.01t                 $ S(alpha,beta) matrix for H in CH2 at 300K
C ---------------------------------------------------------
C  - T400 - Bois (d=0.50 - sapin - ajuste � 0.730 pour marches ...)
M20   1001.60c   -0.06000   & $ H
      6000.60c   -0.50000   & $ C
      7014.60c   -0.00100   & $ N
      8016.60c   -0.43000     $ O
C ---------------------------------------------------------
C  - Am-Be source (d calcul�e = 2.7882) - d=1/(somme(Wf(i)/d(i)) avec d(Be)=1.848, d(Am2O3)=11.77
M21   4009.60c   -0.60000 &  $ Be
      8016.60c   -0.04688 &  $ Am2O3
     95241.60c   -0.35312    $ Active material
C ---------------------------------------------------------
C  - Cf-252 source (d=0.074) - issue des donn�es d'entr�e
M22   8016.60c    0.6      &  $ Cf2O3
     98252.60c    0.4         $ Active material 
C ---------------------------------------------------------
C  - Tubes support - Acier inox (d=7.9)
M23  26000.42c  -72.0  & $ Fe
     24000.42c  -18.0  & $ Cr
     28000.42c  -10.0    $ Ni
C ---------------------------------------------------------
C  - Sources piston et doigt d'etancheite - Aluminium AG3 (US 5455) - (d=2.685)
M24   4009.60c   -8.0E-06  & $ Be
     12000.60c   -0.027    & $ Mg 
     13027.60c   -0.954492 & $ Al
     14000.60c   -0.0025   & $ Si
     22000.60c   -0.00125  & $ Ti
     24000.42c   -0.00125  & $ Cr 
     25055.60c   -0.007    & $ Mn 
     26000.42c   -0.004    & $ Fe
     30000.40c   -0.0025     $ Zn
C ---------------------------------------------------------
C  - Lead cap - Plomb pur (d=11.35)
M25  82000.50c   -1.0        $ Pb
C ---------------------------------------------------------
C  - Tige + support AmBe et Cf + capsule + capot - Acier Z6 CND 17-04 (d=7.7)
M26   6000.60c   -0.00060  & $ C
     24000.42c   -0.16000  & $ Cr
     28000.42c   -0.04000  & $ Ni
     42000.60c   -0.01000  & $ Mo
     26000.42c   -0.78940    $ Fe
C ---------------------------------------------------------
C  - Source container internal Box - Polyethylene (d=0.96)
M27   1001.60c    0.66667    & $ H
      6000.60c    0.33333      $ C
MT27  poly.01t                 $ S(alpha,beta) matrix for H in CH2 at 300K
C ---------------------------------------------------------
C  - Source container external Box - Polyurethane (d=0.96)
M28   1001.60c    0.66667    & $ H
      6000.60c    0.33333      $ C
MT28  poly.01t                 $ S(alpha,beta) matrix for H in CH2 at 300K
C ---------------------------------------------------------
C  - Garde Corps escalier Van Gogh - Tiges - Stainless steel S235JR (d=7.8)
M29   6000.60c   -0.170000  & $ C
      7014.60c   -0.012000  & $ N
     15031.60c   -0.035000  & $ P
     16000.60c   -0.035000  & $ S
     25055.60c   -1.400000  & $ Mn
     29000.50c   -0.350000  & $ Cu
     26000.42c   -0.979980    $ Fe
C ---------------------------------------------------------
C  - Eau Lourde - PNNL 2011 - (d=1.10534)
M30   1002.60c   -0.201133  & $ H2
      8016.60c   -0.798867    $ O16
C ---------------------------------------------------------
C  - Source ejection tube - Aluminium AG3M (US 5754) (d=2.66)
M31  12000.60c   -0.031    & $ Mg
     13027.60c   -0.9495   & $ Al 
     14000.60c   -0.002    & $ Si
     22000.60c   -0.0015   & $ Ti
     24000.42c   -0.003    & $ Cr 
     25055.60c   -0.005    & $ Mn
     26000.42c   -0.004    & $ Fe
     30000.40c   -0.004      $ Zn
C ---------------------------------------------------------
C  - Sources Housing - Stainless steel Z3 CND 18 12 (AISI 316 L) (d=7.96)
M32   6000.60c   -0.00035  & $ C
     14000.60c   -0.0075   & $ Si
     15031.60c   -0.004    & $ P
     16000.60c   -0.003    & $ O
     24000.42c   -0.17     & $ Cr
     25055.60c   -0.02     & $ Mn
     26000.42c   -0.64515  & $ Fe
     28000.42c   -0.125    & $ Ni
     42000.60c   -0.025      $ Mo
C ---------------------------------------------------------
C  - Dural -http://www.goodfellow.com/F/Dural-Aluminium-Cuivre-Magnesium.html (d=2.8)
M33  13027.60c  -95.00     & $ Al
     29000.50c   -4.00     & $ Cu
     25055.60c   -1.00       $ Mn
C ---------------------------------------------------------
C  - Porte-source Cf - Aluminium 6082 https://www.depery-dufour.fr/ (d=2.71)
M34  12000.60c   -0.00900  & $ Mg
     13027.60c   -0.96250  & $ Al
     14000.60c   -0.01000  & $ Si
     22000.60c   -0.00100  & $ Ti
     24000.42c   -0.00250  & $ Cr
     25055.60c   -0.00700  & $ Mn
     26000.42c   -0.00500  & $ Fe
     29000.50c   -0.00100  & $ Cu
     30000.40c   -0.00200    $ Zn
C ---------------------------------------------------------
C  - Sphere Cadmium (d=8.69)
M35  48000.42c   -1.00       $ Cd
C ---------------------------------------------------------
C  - Diodes - Cu/Zn = 70/30 (d=8.386)
M36  29000.50c   -0.70000  & $ Cu
     30000.40c   -0.30000    $ Zn
C ---------------------------------------------------------
C  - sphere - Steel, Stailess 304 (d=8.0)
M37   6000.60c   -0.00040  & $ C
     14000.60c   -0.00500  & $ Si
     15031.60c   -0.00023  & $ P
     16000.60c   -0.00015  & $ S
     24000.42c   -0.19000  & $ Cr
     25055.60c   -0.01000  & $ Mn
     26000.42c   -0.70173  & $ Fe
     28000.42c   -0.09250    $ Ni
C ---------------------------------------------------------
C  - M�lange Cuivre/Fer + Plastique (50/50) - (d=variable)
C  - d=1.2000 Armoires �lectriques
C  - d=1.4844 Compresseurs
C  - d=0.3493 Ballons compresseurs
C
M38  29000.50c  -25.0   & $ Cu
     26000.42c  -25.0   & $ Fe
      6000.60c  -42.82  & $ C
      1001.60c   -7.18    $ H
C ---------------------------------------------------------
C  - Acier inox + Air (d=variable)
C  - d=0.0694 Armoires vides - Acier inox 100x180x40 50 kg
C  - d=0.1832 Canon + Tube
C    d=0.6250 Armoires local sources
C  - d=0.9240 Caillebotis
C
M39  26000.42c  -72.0  & $ Fe
     24000.42c  -18.0  & $ Cr
     28000.42c  -10.0    $ Ni
C ---------------------------------------------------------
C  - Cible TiD - T400 Ti/D = 1 / 1.58 atomique (d=4.84)
M40  22000.60c   0.38760  & $ Ti
      1002.60c   0.61240    $ H2
C ---------------------------------------------------------
C  - Cablage - M�lange Cuivre + Plastique (50/50) - (d=1.734)
M41  29000.50c  -50.00  & $ Cu
      6000.60c  -42.82  & $ C
      1001.60c   -7.18    $ H
MT41  poly.01t            $ S(alpha,beta) matrix for H in CH2 at 300K
C ---------------------------------------------------------
C  - M�lange Cuivre/Fer + Plastique (50/50) - MOTEURS (d=2.0)
M42  29000.50c  -25.0   & $ Cu
     26000.42c  -25.0   & $ Fe
      6000.60c  -42.82  & $ C
      1001.60c   -7.18    $ H
MT42  poly.01t            $ S(alpha,beta) matrix for H in CH2 at 300K
C ---------------------------------------------------------
C  - Acier de construction + Air (d=variable)
C  - d=1.8962 Structure + renforts Van Gogh
C  - d=2.1614 Pieds P5/P7
C  - d=2.3491 Pieds P6
C  - d=1.8484 Pieds P2
C  - d=1.9869 Pieds P1
C  - d=2.0796 Pieds P3/P4
C  - d=0.4971 Barres marches T400
C  - d=1.7645 Support Canel
C  - d=1.4860 Support canon
C  - d=2.4450 Poteau poutre cam�ra
C  - d=1.7770 Chassis Bloc Source
C  - d=1.9466 Support armoire Bloc Source
C  - d=1.2013 Support T pieds T400
C  - d=1.3800 Van Gogh Structure Bleue Pieds
C  - d=2.1899 Van Gogh Portique Grise Pieds
C
M43  26000.42c  -99.0  & $ Fe  
      6000.60c  -1.00    $ C
C ---------------------------------------------------------
C  - Garde-corps Plateforme Van Gogh - Support Cam�ra - Aluminium 6061-O - PNNL - (d=2.7)
M44  12000.60c   -0.010    & $ Mg
     13027.60c   -0.972    & $ Al 
     14000.60c   -0.006    & $ Si
     22000.60c   -0.00088  & $ Ti
     24000.42c   -0.00195  & $ Cr 
     25055.60c   -0.00088  & $ Mn
     26000.42c   -0.00409  & $ Fe
     29000.50c   -0.00275  & $ Cu
     30000.40c   -0.00146    $ Zn
C ---------------------------------------------------------
C  - Banc Van Gogh - Module d'entrainement - Aluminium AU4G - (d=2.79)
M45  12000.60c   -0.00700  & $ Mg
     13027.60c   -0.93700  & $ Al 
     14000.60c   -0.00600  & $ Si
     22000.60c   -0.00250  & $ Ti
     24000.42c   -0.00100  & $ Cr 
     25055.60c   -0.00700  & $ Mn
     26000.42c   -0.00700  & $ Fe
     29000.50c   -0.03000  & $ Cu
     30000.40c   -0.00250    $ Zn
C ---------------------------------------------------------
C  - Banc Van Gogh - Inox 304L - (d=8.00)
M46   6000.60c   -0.00015  & $ C
     14000.60c   -0.00500  & $ Si
     15031.60c   -0.00023  & $ P
     16000.60c   -0.00015  & $ S
     24000.42c   -0.19000  & $ Cr
     25055.60c   -0.01000  & $ Mn
     26000.42c   -0.69448  & $ Fe
     28000.42c   -0.10000    $ Ni
C ---------------------------------------------------------
C  - Cone d'ombre - Acier phosphat� (d=7.603) - www.ars-metal.com/normes/fil-ressort.pdf
M47   6000.60c   -0.00675  & $ C
     14000.60c   -0.00200  & $ Si
     25055.60c   -0.00850  & $ Mn
     15031.60c   -0.00035  & $ P
     16000.60c   -0.00035  & $ S
     29000.50c   -0.00200  & $ Cu
     26000.42c   -0.98005  $   Fe
C ---------------------------------------------------------
C  - Cone d'ombre - PEHD (CH2 d=0.95)
M48   1001.60c    0.66667  & $ H
      6000.60c    0.33333    $ C
MT48  poly.01t               $ S(alpha,beta) matrix for H in CH2 at 300K 
C ---------------------------------------------------------
C  - Plaques Cam�ra - PVC (C2H3Cl) - (d=1.38)
M53   1001.60c    0.50000  & $ H
      6000.60c    0.33333  & $ C
     17000.60c    0.16667    $ Cl
MT53  poly.01t               $ S(alpha,beta) matrix for H in CH2 at 300K
C ---------------------------------------------------------
C  - Local B�G - Polypropyl�ne (d=0.9)
M55   1001.60c    0.66667    & $ H
      6000.60c    0.33333      $ C
MT55  poly.01t                 $ S(alpha,beta) matrix for H in CH2 at 300K
C ---------------------------------------------------------
C   - Canel Acier (d=7.87)
M56   6000.60c   -0.00030 &
     14000.60c   -0.01000 &
     15031.60c   -0.00045 &
     16000.60c   -0.00030 &
     24000.42c   -0.18500 &
     25055.60c   -0.02000 &
     26000.42c   -0.67145 &
     28000.42c   -0.11250
C ---------------------------------------------------------
C  - Canel - uranium appauvri (d=19.06)
M57  92238.60c   -0.9975 &
     92235.60c   -0.0025
C ---------------------------------------------------------
C  - Canel - porte-cible Al (d=2.69)
M58  13027.60c    1.00
C ---------------------------------------------------------
C  - Canel - Void dans porte-cible (d=1.300E-06)
M59   1001.60c   -0.000556   & $ H
      6000.60c   -0.000124   & $ C
      7014.60c   -0.754848   & $ N
      8016.60c   -0.231652   & $ O
     18000.42c   -0.012820     $ Ar
C ---------------------------------------------------------
C  - Canel - Backing - Cu (d=8.96)
M60  29000.50c   -1.0
C ---------------------------------------------------------
C  - Canel - Eau de refroidissement (d=1.0)
M61   1001.60c    0.667 &
      8016.60c    0.333    $ Water (H2O)
C ---------------------------------------------------------
C  - Canel - Inside fission chamber - Al low density (d=2.00)
M62  13027.60c   -1.0 
C ---------------------------------------------------------
C  - Canel - ICRU tissue sustitute (Schu, Sieb, RPD 92) - Phantom (d=1.00)
M63   1001.60c   -0.101     & $ H
      8016.60c   -0.762     & $ O16
      6012.50c   -0.111     & $ C12
      7014.60c   -0.026       $ N14
C ---------------------------------------------------------
C  - Ballon T400 - Gas SF6 6 bars (d=0.03597)
M64   9019.60c    6.0  &
     16000.60c    1.0  $  GAS=1
C ---------------------------------------------------------
C *************************************************************************** C
C ***************************** �L�MENTS INS�R�S **************************** C
C *************************************************************************** C
C **    La carte des mat�riaux independante de celles d'AMANDE et CEZANE   ** C
C ** La carte est � ins�rer dans le fichier utilisant les �l�ments ins�r�s ** C
C    Liste des mat�riaux :
C ----- M502 - Air - d=1.3E-03
C ----- M503 - ICRU tissue sustitute
C ----- M504 - Vide dans la ligne de faisceau AMANDE PC - d=1.0E-07
C ----- M505 - Acier inox - d=7.9
C ----- M506 - Aluminium - d=2.7
C       ...
C ----- M515 - Cible Tungsten - d=19.35
C ----- M516 - Plastique CH2 - d=0.96
C ----- M517 - Laiton PC AMANDE - d=8.40
C ----- M518 - Cadmium - d=8.65
C ----- M519 - Borated paraffine - d=0.89
C ----- M520 - He-3
C ----- M521 - Mousse polyurethane PC AMANDE - d=0.06
C ----- M522 - Fer Aimant PC AMANDE - d=7.86
C ----- M523 - Melange He3/Methane
C       ...
C ----- M526 - Cone d'ombre - Acier phosphat� - d=7.603
C ----- M527 - Cone d'ombre - PEHD CH2 - d=0.95
C       ...
C ----- M530 - CR39-LDRI - d=1.31
C ----- M531 - Plexi CR39-LDRI d=1.19
C ----- M532 - C�ramic Al2O3 d=3.85
C ----- M533 - PCB = Carte electronique d=3.5
C ----- M534 - Disque avant BC501 !!! ATTENTION - Mat�riau inconnu !!!
C ----- M535 - Liquide Scintillant BC501A - d=0.874
C ----- M536 - Plexiglasse C5H8O2 - d=1.2
C ----- M537 - Photomultiplicateur BC501 - idem M533
C ----- M538 - Alliage Aluminium 2017A - d=2.79
C ----- M539 - 95% He + 5% CO2  �TPC - d=0.0001723
C ----- M540 - Acier Inoxydable aust�nique 1.4307 - d=8.0
C ----- M541 - Acier Inoxydable - d=8.03
C ----- M542 - Viton �TPC - d=2.06
C ----- M543 - PEEK �TPC - d=1.3
C ----- M544 - Polycarbonate (C16H14O3) - d=1.2
C ----- M545 - Cuivre naturel - d=8.93
C ----- M546 - Acier 430F (1.4104) - d=7.7
C ----- M547 - M�lange 50% M532 + 50% M546 - d=5.78
C ----- M548 - Aluminium type EN AW-5083 - d=2.66
C ----- M549 - M�lange 50% Acier AISI 304 + 50% Aluminium EN AW-5083 - d=5.33
C ----- M550 - Caoutchouc - d=0.99
C ----- M551 - Alliage Aluminium 2017A - d=2.8
C *************************************************************************** C
C ---------------------------------------------------------               
C  - Air - d=1.3E-03              
M502    8016.60c     0.20000   & $ O
        7014.60c     0.80000     $ N
C ---------------------------------------------------------               
c  - ICRU tissue sustitute (Schu, Sieb, RPD 92)               
M503    1001.60c    -0.10100   & $ H
        8016.60c    -0.76200   & $ O16
        6012.50c    -0.11100   & $ C12
        7014.60c    -0.02600     $ N14
C ---------------------------------------------------------               
C  - Vide dans la ligne de faisceau AMANDE PC - d=1.0E-07               
M504    8016.60c     0.20000   & $ O
        7014.60c     0.80000     $ N
C ---------------------------------------------------------
C  - Acier inox (d=7.9)               
M505   26000.42c   -72.00000   & $ Fe
       24000.42c   -18.00000   & $ Cr
       28000.42c   -10.00000     $ Ni
C ---------------------------------------------------------               
C  - Support Cone d'ombre, Support BC501, Gaines de ventilation, Vannes BSS ... - Aluminium - d=2.7               
M506   13027.60c   100.00000     $ Al
C ---------------------------------------------------------               
C  - Cible Tungsten - d=19.35               
M515   74000.55c    -1.00000     $ W
C ---------------------------------------------------------               
C  - Plastique CH2 - d=0.96               
M516    1001.60c     0.66667   & $ H
        6000.60c     0.33333     $ C
MT516   poly.01t                 $ S(alpha,beta) matrix for H in CH2 at 300K
C ---------------------------------------------------------               
C  - Laiton PC AMANDE - d=8.40               
M517   29000.50c    -0.67000   & $ Cu
       30000.42c    -0.29000   & $ Zn
       82000.42c    -0.03000   & $ Pb
       50000.42c    -0.01000     $ Sn
C ---------------------------------------------------------               
C  - Cadmium - d=8.65
M518   48000.42c     1.00000     $ Cd
C ---------------------------------------------------------               
C  - Borated paraffine - d=0.89
M519    1001.60c     0.81700   & $ H
        6000.60c     0.13300   & $ C
        5010.60c     0.05000     $ B
C ---------------------------------------------------------               
C  - He-3               
M520    2003.60c     1.00000     $ He-3
C ---------------------------------------------------------               
C - Mousse polyurethane PC AMANDE - d=0.06               
M521    1001.60c    -0.79000   & $ H
        8016.60c   -53.75000   & $ O16
        6012.50c    -9.49000   & $ C12
        7014.60c   -35.97000     $ N14
C ---------------------------------------------------------               
C  - Fer Aimant PC AMANDE - d=7.86               
M522   26056.60c    -1.00000     $ Fe56
C ---------------------------------------------------------  
C - Melange He3/Methane Zone Active
M523    1001       -0.125659   & $ H
        6000       -0.374341   & $ C
        2003       -0.5          $ He3
C ---------------------------------------------------------
C  - Cone d'ombre - Acier phosphat� (d=7.603) - www.ars-metal.com/normes/fil-ressort.pdf               
M526    6000.60c    -0.67500   & $ C
       14000.60c    -0.20000   & $ Si
       25055.60c    -0.85000   & $ Mn
       15031.60c    -0.03500   & $ P
       16000.60c    -0.03500   & $ S
       29000.50c    -0.20000   & $ Cu
       26000.42c   -98.00500     $ Fe
C ---------------------------------------------------------               
C  - Cone d'ombre - PEHD CH2 - d=0.95               
M527    1001.60c     0.66667   & $ H
        6000.60c     0.33333     $ C
MT527   poly.01t                 $ S(alpha,beta) matrix for H in CH2 at 300K  
C ---------------------------------------------------------
C  - CR39-LDRI - d=1.31
M530    1001.60c     18.00000   & $ H
        6000.60c     12.00000   & $ C
        8016.60c      7.00000     $ O
C ---------------------------------------------------------               
C  - Plexi CR39-LDRI - d=1.19
M531    1001.60c     0.080538   & $ H
        6000.60c     0.599848   & $ C
        8016.60c     0.319614     $ O
C ---------------------------------------------------------               
C  - C�ramic Al2O3 ?               
M532   13027.60c     0.40000   & $ Al
        8016.60c     0.60000     $ O
C ---------------------------------------------------------               
C  - PCB = Carte electronique (issue de �TPC) - densit� suppos�e d=3.5               
M533   29063.60c     0.08690   & $ Cu63
       29065.60c     0.03730   & $ Cu65
       13027.60c     0.01810   & $ Al27
       26056.60c     0.01960   & $ Fe56
       82000.42c     0.01020   & $ Pb-nat
       30000.42c     0.00710   & $ Zn-nat
       28058.60c     0.00710   & $ Ni58
       50000.42c     0.01615   & $ Sn-nat
       51000.42c     0.00005   & $ Sb-nat
       14028.66c     0.16350   & $ Si28
        8016.60c     0.32650   & $ O16
        6000.60c     0.10250   & $ C-nat
        1001.60c     0.20500     $ H1
C ---------------------------------------------------------               
C  - Disque avant BC501 !!! ATTENTION - Mat�riau inconnu !!!               
M534   13027.60c   100.00000     $ Inconnu
C ---------------------------------------------------------               
C  - Liquide Scintillant BC501A - d=0.874) - Donnees extraite de la notice saint gobain               
M535    6000.60c     3.98000   & $ C
        1001.60c     4.82000     $ H
C ---------------------------------------------------------               
C  - Guide Lumi�re BC501 - Plexiglasse C5H8O2 - d=1.2
M536    6000.60c     5.00000   & $ C
        1001.60c     8.00000   & $ H
        8016.60c     2.00000     $ O
C ---------------------------------------------------------               
C  - Photomultiplicateur BC501 - Carte electronique (issue de �TPC) - densit� suppos�e d=3.5               
M537   29063.60c     0.08690   & $ Cu63
       29065.60c     0.03730   & $ Cu65
       13027.60c     0.01810   & $ Al27
       26056.60c     0.01960   & $ Fe56
       82000.42c     0.01020   & $ Pb-nat
       30000.42c     0.00710   & $ Zn-nat
       28058.60c     0.00710   & $ Ni58
       50000.42c     0.01615   & $ Sn-nat
       51000.42c     0.00005   & $ Sb-nat
       14028.66c     0.16350   & $ Si28
        8016.60c     0.32650   & $ O16
        6000.60c     0.10250   & $ C-nat
        1001.60c     0.20500     $ H1
C ---------------------------------------------------------               
C  - Alliage Aluminium 2017A �TPC - Al, Cu-nat, Pb, Mn55, Mg-nat, Fe-nat, Si-nat, Zn-nat - d=2.79 - http://www.euralliage.com/2017A.htm               
M538   13027.42c     0.93050   & $ Al27
       29000.50c     0.04000   & $ Cu
       25055.66c     0.00700   & $ Mn55
       12000.42c     0.00700   & $ Mg-nat
       26056.66c     0.00700   & $ Fe56
       14028.66c     0.00500   & $ Si28
       24052.66c     0.00100   & $ Cr52
       30000.42c     0.00250     $ Zn
C ---------------------------------------------------------               
C  - 95% He + 5% CO2  �TPC - d=0.0001723 � 700mbar. Pour 700 mbar --> d(He)=0.00011488 et d(CO2)=0.00126365               
M539    2004.66c     0.95000   & $ He
        6000.66c     0.01670   & $ C
        8016.66c     0.03330     $ O
C ---------------------------------------------------------               
C  ---- Acier Inoxydable aust�nique 1.4307 �TPC  Mn-nat, P31 et S16 d=8.0 - http://www.eqx.com/datasheets/Stainless-Steel_1.4307-304L_35.asmx               
M540   26056.66c    0.709725   & $ Fe56
       24052.66c    0.185000   & $ Cr52
       28058.66c    0.090000   & $ Ni58
       25055.66c    0.010000   & $ Mn55
       14028.66c    0.005000   & $ Si28
       15031.66c    0.000200   & $ P31
       16032.66c    0.000075     $ S32
C ---------------------------------------------------------              
C  - Acier Inoxydable �TPC  Fe-nat, Cr-nat, Ni-nat, Mo-nat, Si-nat et Mn-nat - d=8.03               
M541   26056.66c     0.65500   & $ Fe
       24052.66c     0.17000   & $ Cr
       28058.66c     0.12000   & $ Ni
       42000.66c     0.02500   & $ Mo
       14028.66c     0.01000   & $ Si
       25055.66c     0.02000     $ Mn
C ---------------------------------------------------------               
C  - Viton �TPC - d=2.06 - THV (Tetrafluoroethylene C2F4 d=1052, Hexafluoropropylene C3F6 d=1.33 and Vinylidene fluoride C2H2F2 d=1.78)               
M542    9019.66c     0.57200   & $ F
        6000.66c     0.33300   & $ C
        1001.66c     0.09500     $ H
C ---------------------------------------------------------               
C  - PEEK �TPC - d=1.3               
M543    8016.66c     0.08820   & $ O
        6000.66c     0.55880   & $ C
        1001.66c     0.35300     $ H
C ---------------------------------------------------------               
C  - Polycarbonate (C16H14O3) - d=1.2               
M544    6000.66c     0.00040   & $ C-nat
        1001.66c     0.20500   & $ H1
        8016.66c     0.03330     $ O
C ---------------------------------------------------------               
C  - Cuivre naturel - d=8.93               
M545   29000.50c     1.00000     $ Cu-nat
C ---------------------------------------------------------               
C  - Acier 430F (1.4104) �TPC - d=7.7   http://www.coulton.com/res/TN5FCXAIIV5d-E.pdf               
M546    6000.66c    0.001350   & $ C-nat
       24052.66c    0.165000   & $ Cr52
       26056.66c    0.814950   & $ Fe56
       25055.66c    0.007500   & $ Mn55
       15031.66c    0.000200   & $ P31
       16032.66c    0.002000   & $ S32
       14028.66c    0.005000   & $ Si28
       42000.66c    0.004000     $ Mo
C ---------------------------------------------------------               
C  - M�lange 50% Acier 430F (1.4104) et 50% Al2O3 (d=3.85) �TPC - d=5.78               
M547   13027.42c    0.200000   & $ Al27
        8016.66c    0.300000   & $ O16
        6000.66c    0.000675   & $ C-nat
       24052.66c    0.082500   & $ Cr52
       26056.66c    0.407475   & $ Fe56
       25055.66c    0.003750   & $ Mn55
       15031.66c    0.000100   & $ P31
       16032.66c    0.001000   & $ S32
       14028.66c    0.002500   & $ Si28
       42000.66c    0.002000     $ Mo
C ---------------------------------------------------------               
C  - Aluminium type EN AW-5083 �TPC - d=2.66               
M548   13027.42c     0.92900   & $ Al27
       14028.66c     0.00400   & $ Si28
       26056.66c     0.00400   & $ Fe56
       29000.50c     0.00100   & $ Cu
       25055.66c     0.00700   & $ Mn55
       12000.42c     0.04500   & $ Mg-nat
       24052.66c     0.00600   & $ Cr52
       30000.42c     0.00250   & $ Zn-nat
       22000.66c     0.00150     $ Ti-nat
C ---------------------------------------------------------               
C  - M�lange �TPC 50% Acier AISI 304 et 50% Aluminium EN AW-5083 - d=5.33               
M549    6000.66c    0.000175   & $ C-nat
       24052.66c    0.095500   & $ Cr52
       26056.66c    0.352900   & $ Fe56
       25055.66c    0.008500   & $ Mn55
       28058.66c    0.048750   & $ Ni58
       15031.66c    0.000125   & $ P31
       16032.66c    0.000050   & $ S32
       14028.66c    0.004500   & $ Si28
       13027.42c    0.464500   & $ Al27
       29000.50c    0.000500   & $ Cu
       12000.42c    0.022500   & $ Mg-nat
       30000.42c    0.001250   & $ Zn-nat
       22000.66c    0.000750     $ Ti-nat
C ---------------------------------------------------------               
C  - Caoutchouc �TPC - d=0.99               
M550    1001.66c     0.61500   & $ H
        6000.66c     0.38500     $ C
C ---------------------------------------------------------               
C  - Alliage Aluminium 2017A �TPC - d=2.8   http://www.metaux-detail.com/pdf/alu/2017A.pdf               
M551   13027.42c     0.99939   & $ Al27
       29000.50c     0.04000   & $ Cu
       24052.66c     0.00100   & $ Cr52
       26056.66c     0.00350   & $ Fe56
       25055.66c     0.00700   & $ Mn55
       12000.42c     0.00700   & $ Mg-nat
       30000.42c     0.00250     $ Zn-nat

