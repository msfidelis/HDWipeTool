#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
__author__ = 'matheus'
__git___ = 'github.com/msfidelis'


def banner ():
    print """
    __  ______ _       ___               ______            __
   / / / / __ \ |     / (_)___  ___     /_  __/___  ____  / /
  / /_/ / / / / | /| / / / __ \/ _ \     / / / __ \/ __ \/ /
 / __  / /_/ /| |/ |/ / / /_/ /  __/    / / / /_/ / /_/ / /
/_/ /_/_____/ |__/|__/_/ .___/\___/    /_/  \____/\____/_/
                      /_/

        LINUX PARTITIONS AND HARD DRIVE ERASER TOOL
                CODED BY: MATHEUS FIDELIS

    """
    getopts()


def apagahd(partition,jumps):

    jumps   = int(jumps)
    numpart = '/dev/zero'

    #Comandos que vão ser executados no Shell
    ddcmd   = 'dd if=%s of=%s bs=1M & pid=$!' % (numpart, partition)

    #Desmonta a partição
    #umount  = 'umount %s' % partition

    mkvfat  = 'mkfs.vfat    %s -I'  % partition     # Formata em Filesystem VFAT
    mkdos   = 'mkfs.msdos   %s -I'  % partition     # Formata em Filesystem MSDOS
    mkntfs  = 'mkfs.ntfs    %s -I'  % partition     # Formata em Filesystem NTFS
    mkvext2 = 'mkfs.ext2    %s'     % partition     # Formata em Filesystem ext2
    mkvext3 = 'mkfs.ext3    %s'     % partition     # Formata em Filesystem ext3
    mkvext4 = 'mkfs.ext4    %s'     % partition     # Formata em Filesystem ext4
    mkminix = 'mkfs.minix   %s'     % partition     # Formata em Filesystem Minix


    #Executa uma série de intruções de wipe de disco de acordo com o numero de saltos determinados
    print "Executando o salto com %s saltos" % jumps
    count = 0
    while (count < jumps):
        count = count + 1
        print "[*] Executando %sº salto" % count

        #Executa a formatação da partição em massa - Não aconselhavel utilizar em SSD, sério....

        print "[*] Executando a formatação em massa de FileSystem"

        print "[!] Executando a formatação da partição da partição para vfat"
        subprocess.check_output(mkvfat, shell=True)

        print "[!] Executando a formatação da partição da partição para ext2"
        subprocess.check_output(mkvext2, shell=True)

        print "[!] Executando a formatação da partição da partição para MSDOS"
        subprocess.check_output(mkdos, shell=True)

        print "[!] Executando a formatação da partição da partição para ext3"
        subprocess.check_output(mkvext3, shell=True)

        print "[!] Executando a formatação da partição da partição para NTFS"
        subprocess.check_output(mkntfs, shell=True)

        print "[!] Executando a formatação da partição da partição para MINIX"
        subprocess.check_output(mkminix, shell=True)

        print "[!] Executando a formatação da partição da partição para ext4"
        subprocess.check_output(mkvext4, shell=True)

        print "[!] Executando a formatação da partição da partição para vfat"
        subprocess.check_output(mkvfat, shell=True)

        print "[!] Executando a formatação da partição da partição para ext4"
        subprocess.check_output(mkvext4, shell=True)


        #Executa a cópia de baixo nível bit a bit de uma partição cheia de bits nulos com o DD
        print "[!] Executando a cópia bit a bit de valores nulos para a partição"
        subprocess.check_output(ddcmd, shell=True)



def getopts():

    #Usuário digita a partição crua, ex: sda, sdb, sdc e etc."
    partition = raw_input("Informe a partição desejada (Ex: sda, sdb, sdc..): ")
    partition = '/dev/%s' % partition

    #Pega o numero de saltos
    jumps = raw_input("Informe o numero de saltos a serem executados (Recomendado: 2): ")

    #Inicia o processo de wipe 
    apagahd(partition,jumps)


banner()
