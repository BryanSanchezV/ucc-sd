CREATE TABLE public.dummy (
	id serial4 NOT NULL,
	"name" varchar(30) NULL
);

INSERT INTO public.dummy (id, "name") VALUES(nextval('dummy_id_seq'::regclass), 'Bryan Stiven');
INSERT INTO public.dummy (id, "name") VALUES(nextval('dummy_id_seq'::regclass), 'Juan Felipe');
INSERT INTO public.dummy (id, "name") VALUES(nextval('dummy_id_seq'::regclass), 'Sebastian');
INSERT INTO public.dummy (id, "name") VALUES(nextval('dummy_id_seq'::regclass), 'Martinez');

INSERT INTO public.dummy (id, "name") VALUES(nextval('dummy_id_seq'::regclass), 'Alexandra');
INSERT INTO public.dummy (id, "name") VALUES(nextval('dummy_id_seq'::regclass), 'Ibeth');
INSERT INTO public.dummy (id, "name") VALUES(nextval('dummy_id_seq'::regclass), 'Stefania');


SELECT id, "name" FROM public.dummy;
