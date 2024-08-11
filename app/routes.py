from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('main_html.html')

@bp.route('/complemento')
def complemento():
    return render_template('complemento.html')

@bp.route('/vaso_de_leche')
def vaso_de_leche():
    return render_template('vaso_de_leche.html')

@bp.route('/inicia_sesion')
def inicia_sesion():
    return render_template('inicia_sesion.html')

@bp.route('/quejas')
def quejas():
    return render_template('Quejas.html')